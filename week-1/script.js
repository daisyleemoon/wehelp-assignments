const showMenu = () => {
  let menuUl = document.getElementById("navbar");
  menuUl.classList.toggle("ulMenu");
};

const url =
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";

const addCards = () => {
  let cardCounts = document.getElementById("photoBox").childElementCount;
  let loadSize = getPageSize(cardCounts);
  attractionsInfo.slice(cardCounts, cardCounts + loadSize).forEach(addCard);
};

const pageSize = 8;
const getPageSize = (cardCounts) => {
  let remainingCounts = totalCounts - cardCounts;
  if (remainingCounts > pageSize) {
    return pageSize;
  } else {
    let loadButton = document.getElementById("loadButton");
    loadButton.value = "No More!";
    return remainingCounts;
  }
};

const addCard = (attraction) => {
  let { imgUrl, caption } = parseAttractionsInfo(attraction);
  let newDiv = document
    .getElementById("photoBox")
    .appendChild(document.createElement("div"));
  let newImgSec = newDiv.appendChild(document.createElement("img"));
  let newPara = newDiv.appendChild(document.createElement("p"));
  newImgSec.src = imgUrl;
  newPara.textContent = caption;
  newDiv.setAttribute("class", "photoCard");
};

const parseAttractionsInfo = (attraction) => {
  let imgUrl = `https${attraction.file.split("https")[1]}`;
  let caption = attraction.stitle;

  return { imgUrl, caption };
};

fetch(url)
  .then((res) => res.json())
  .then((data) => data.result.results)
  .then((results) => {
    attractionsInfo = results;
    totalCounts = results.length;
  })
  .then(addCards)
  .catch(console.log);
