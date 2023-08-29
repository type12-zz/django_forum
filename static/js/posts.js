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

const likeIcons = document.querySelectorAll('.like-icon');

likeIcons.forEach(likeIcon => {
  let numOfLikes = 0;
  let hasBeenLiked = false;
  const likeNumSpan = likeIcon.nextElementSibling;
  likeIcon.addEventListener('click', () => {
    let numOfLikes = parseInt(likeNumSpan.textContent) || 0;
    numOfLikes++;
    likeNumSpan.textContent = numOfLikes;
    if(!hasBeenLiked){
      likeIcon.src ='static/img/filled_heart.png'; //set the new src of the image
      hasBeenLiked = true;
    }
  });
});

