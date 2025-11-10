// Syntax highlighting with highlight.js.
document$.subscribe(() => {
  hljs.highlightAll()
})
// Table sorting.
document$.subscribe(function() {
  var tables = document.querySelectorAll("article table:not([class])")
  tables.forEach(function(table) {
    new Tablesort(table)
  })
})