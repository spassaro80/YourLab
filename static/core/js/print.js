function downloadPDFWithBrowserPrint() {
    window.print();
  }
  document.querySelector('#browserPrint').addEventListener('click', downloadPDFWithBrowserPrint);