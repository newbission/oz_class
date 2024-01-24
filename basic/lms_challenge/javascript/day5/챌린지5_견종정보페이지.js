const apiRandomDogs = 'https://dog.ceo/api/breeds/image/random/42';
const apiAllBreeds = 'https://dog.ceo/api/breeds/list/all';
const request1 = new XMLHttpRequest();
const request2 = new XMLHttpRequest();

const header = document.getElementById('header');
const main = document.getElementById('main');
const input = document.getElementById('filter-text');
const button = document.getElementById('filter-button');
const select = document.getElementById('filter-select');
const more = document.getElementById('more');
const tothetop = document.getElementById('tothetop');
const reset = document.getElementById('reset');

let respondedDogs = [];

window.addEventListener('load', () => {
  //  강아지 사진 뿌리기
  // getNewDogsData();

  request2.open('get', apiAllBreeds);
  request2.addEventListener('load', () => {
    const response = JSON.parse(request2.response);
    Object.keys(response.message).forEach((item) => {
      const option = document.createElement('option');
      option.innerText = item;
      option.value = item;
      select.appendChild(option);
    });
  });
  request2.send();
});

button.addEventListener('click', () => {
  main.innerHTML = '';
  const filteredDogs = getFilteredDogs(input.value);
  for (const dog of filteredDogs) {
    printDogsImg(dog);
  }
});

select.addEventListener('change', () => {
  main.innerHTML = '';
  const filteredDogs = getFilteredDogs(select.value);
  for (const dog of filteredDogs) {
    printDogsImg(dog);
  }
});

more.addEventListener('click', () => {
  getNewDogsData();
});

tothetop.addEventListener('click', () => {
  window.scrollTo({top: 0})
})

reset.addEventListener('click', () => {
  main.innerHTML = '';
  respondedDogs = [];
  getNewDogsData();
});

function getNewDogsData() {
  request1.open('get', apiRandomDogs);
  request1.addEventListener('load', requestHandler);
  request1.send();
}

function requestHandler() {
  JSON.parse(request1.response).message.forEach((item) => {
    respondedDogs.push(item);
    printDogsImg(item);
  });
  request1.removeEventListener('load', requestHandler);
  console.log(respondedDogs.length);
}

function getFilteredDogs(value) {
  return respondedDogs.filter((item) => item.indexOf(value) !== -1);
}

function printDogsImg(item) {
  const dogImgDiv = document.createElement('div');
  dogImgDiv.classList.add('flex-item');
  dogImgDiv.innerHTML = `
    <img src=${item}>
  `;
  main.appendChild(dogImgDiv);
}
