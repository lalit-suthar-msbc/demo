function resetSelect(e) {
  console.log('The value was ' + this.value);
  this.selectedIndex = 0;
}

window.onload = function() {
  document.querySelector('select').addEventListener('change', resetSelect, false);
}