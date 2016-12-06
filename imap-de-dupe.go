// package imap-de-dupe will process a given fdupes output and intelligently
// move detected duplicates to a specific directory.
//
// Duplicates are kept based on a preferred directory structure. Only one
// email is kept in its original location, based on e_paths preference.
package main

import (
	"bufio"
	"fmt"
  "path"
	"log"
	"os"
	"strings"
)

// Where your fdupes output is
// find USER_MAIL -type d -name cur -print0 | xargs -0 /usr/bin/fdupes -n > out
// If you think you have dupes in new, then also run for new
const fdupes_file_dump = "/tmp/cur-dupes"
// Where to move your dupes, create standard maildir (dir/{cur,new,tmp})
const dupe_move = "/USER/Maildir/.detected-dupes/cur"

func main() {
  // Preference for directories in which to keep email. Here, if a dupe is
  // detected in Computer and Shopping, Computer is kept. If no preferences are
  // specified, the first duplicate mail to appear is choosen.
  e_paths := excludedPaths{path: []string{
		"gmail-archive.Computer",
		"gmail-archive.Shopping",
		"gmail-archive.Travel",
		"gmail-archive.Drafts",
		"gmail-archive.Sent",
	}}
	file, err := os.Open(fdupes_file_dump)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var fdupe_matches []singleFdupeMatch
	var matches []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		if scanner.Text() == "" {
			fdupe_matches = append(fdupe_matches, singleFdupeMatch{all: matches})
			matches = []string{}
		} else {
			matches = append(matches, scanner.Text())
		}
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	var keepers []string
	var discards []string
	for _, fdupes := range fdupe_matches {
		fdupes.Filter(e_paths)
		keepers = append(keepers, fdupes.keeper)
		discards = append(discards, fdupes.Discard()...)
	}
	fmt.Printf("Found %v duplicate email groups.\n", len(fdupe_matches))
	fmt.Println("Keeping these duplicates:")
	for _, keeper := range keepers {
		fmt.Println(keeper)
	}
	fmt.Printf("\n\nMoving %v duplicates.\n", len(discards))
	for _, file := range discards {
    target := path.Join(dupe_move, path.Base(file))
    fmt.Printf("%v => %v\n", file, target)
    _, err := os.Stat(target)
    if err != nil {
      if os.IsNotExist(err) {
        err := os.Rename(file, path.Join(dupe_move, path.Base(file)))
        if err != nil {
          log.Fatal(err)
        }
      } else {
        log.Fatal(err)
      }
    }
	}
}

// slices of file paths to 'exclude' or keep a copy of mail for
// These should be created in order of keep preference (first
// listed match wins).
type excludedPaths struct {
	path []string
}

// reciever for excludedPaths to determine if a given file string is
// excluded. Returns boolean true for exclude, false otherwise.
func (p *excludedPaths) Excluded(file string) bool {
	for _, excluded_path := range p.path {
		if strings.Contains(file, excluded_path) {
			return true
		}
	}
	return false
}

// receiver for excludedPaths to determine the preferred file
// path for a slice of file paths. Returns string preferred file path or nil.
func (p *excludedPaths) PreferredFile(list []string) string {
	for _, path := range p.path {
		for _, file := range list {
			if strings.Contains(file, path) {
				return file
			}
		}
	}
	return ""
}

// slices of file paths that have matched from fdupes.
// these are group together and separated by a blank line.
type singleFdupeMatch struct {
	all          []string
	excluded     []string
	non_excluded []string
	keeper       string
}

// reciever for singleMatch to filter out messages for a given set of matches
// Initially keeps all files that are in excluded paths, then prefers the
// first excluded path for the final file to keep.
func (f *singleFdupeMatch) Filter(e excludedPaths) {
	for _, match_file := range f.all {
		if e.Excluded(match_file) {
			f.excluded = append(f.excluded, match_file)
		} else {
			f.non_excluded = append(f.non_excluded, match_file)
		}
	}
	// no excluded files in the list (no preference), grab the first one
	if len(f.excluded) == 0 {
		f.keeper = f.all[0]
		return
		// There are excluded files, grab the first by preference.
	} else {
		f.keeper = e.PreferredFile(f.excluded)
		return
	}
}

// reciever for singleFdupeMatch to generate a list of files to discard,
// assuming keeper is set. If no keeper is set, all files are discarded.
// Returns a slice of strings containing files to discard.
func (f *singleFdupeMatch) Discard() []string {
	var discards []string
	for _, file := range f.all {
		if f.keeper != file {
			discards = append(discards, file)
		}
	}
	return discards
}
