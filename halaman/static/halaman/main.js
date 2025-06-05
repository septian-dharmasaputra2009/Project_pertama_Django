function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const main = document.getElementById("main");

  if (sidebar && main) {
    sidebar.classList.toggle("show");
    sidebar.classList.toggle("hide");
    main.classList.toggle("full");
  } else {
    console.error("Element sidebar atau main tidak ditemukan!");
  }
}

window.addEventListener("DOMContentLoaded", function () {
  const sidebar = document.getElementById("sidebar");
  const main = document.getElementById("main");

  sidebar.classList.add("hide");
  sidebar.classList.remove("show");
  main.classList.add("full");
});