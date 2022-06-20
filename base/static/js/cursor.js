let cursor = document.querySelector(".cursor");
let cursorPointer = document.querySelector(".cursor-pointer");
let links = document.querySelectorAll("a");
let links1 = document.querySelectorAll("input");
let links2 = document.querySelectorAll("textarea");
let links3 = document.querySelectorAll("button");
let links4 = document.querySelectorAll("label");
let links5 = document.querySelectorAll("img");

document.addEventListener("mousemove", (e) => {
  cursor.style.top = e.clientY + -12 + "px";
  cursor.style.left = e.clientX + -12 + "px";
});

document.addEventListener("mousemove", (e) => {
  cursorPointer.style.top = e.clientY + "px";
  cursorPointer.style.left = e.clientX + "px";
});

document.addEventListener("click", () => {
  cursor.classList.add("cursorClick");
  setTimeout(() => {
    cursor.classList.remove("cursorClick");
  }, 600);
});

links.forEach((link) => {
  link.addEventListener("mouseover", () => {
    cursor.classList.add("backgroundBlack");
  });

  link.addEventListener("mouseleave", () => {
    cursor.classList.remove("backgroundBlack");
  });
});

links1.forEach((link) => {
  link.addEventListener("mouseover", () => {
    cursor.classList.add("backgroundWhite");
  });

  link.addEventListener("mouseleave", () => {
    cursor.classList.remove("backgroundWhite");
  });
});

links2.forEach((link) => {
  link.addEventListener("mouseover", () => {
    cursor.classList.add("backgroundWhite");
  });

  link.addEventListener("mouseleave", () => {
    cursor.classList.remove("backgroundWhite");
  });
});

links3.forEach((link) => {
  link.addEventListener("mouseover", () => {
    cursor.classList.add("backgroundWhite");
  });

  link.addEventListener("mouseleave", () => {
    cursor.classList.remove("backgroundWhite");
  });
});

links4.forEach((link) => {
  link.style.zIndex = "120";
  link.addEventListener("mouseover", () => {
    cursor.classList.add("backgroundBlack");
  });

  link.addEventListener("mouseleave", () => {
    cursor.classList.remove("backgroundBlack");
  });
});

links5.forEach((link) => {
  link.addEventListener("mouseover", () => {
    cursor.classList.add("backgroundImg");
  });

  link.addEventListener("mouseleave", () => {
    cursor.classList.remove("backgroundImg");
    cursorPointer.classList.remove("cursorPointerNone");
  });
});
