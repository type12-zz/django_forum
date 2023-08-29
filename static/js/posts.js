//------------------------------
//   JavaScript for Post Page  -
//------------------------------

const menuIcons = document.querySelectorAll('.menu_icon');

menuIcons.forEach(icon => {
  icon.addEventListener('click', () => {
    const menu = icon.nextElementSibling;
    if(menu.style.display === 'none') {
      menu.style.display = 'block';
    } else {
      menu.style.display = 'none'; 
    }
  });
});

const likeIcons = document.querySelectorAll('.like_icon');

