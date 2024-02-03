// DOM
const dataTable = document.getElementById('data-table');
const checkAllEl = document.getElementById('check-all');

// Data
const DISPLAY_NUMBER = 20;

let isCheckAllClick = false;

/**
 * 필수정보
 *
 * 카테고리, 브랜드, 상품명, 가격,
 * 성별, 등록일자
 */

/**
 * 더미에 들어갈 데이터 내용
 */
const fashionData = {
  genders: ['공용', '남성', '여성'],
  categories: ['상의', '하의', '신발', '패션잡화'],
  brands: [
    'Nike',
    'Adidas',
    'Gucci',
    'Supreme',
    'Zara',
    'Puma',
    'Converse',
    'Fila',
    'Balenciaga',
    'Vans',
  ],
  products: [
    '에어포스 1',
    '트랙 팬츠',
    '로고 티셔츠',
    '슬립온 스니커즈',
    '베이직 모자',
    '후드 스웨트셔츠',
    '스키니 진',
    '버켄스탁 샌들',
    '체크 무스탕',
    '구찌 목걸이',
  ],
  prices: [
    '390,000',
    '45,000',
    '29,000',
    '120,000',
    '18,000',
    '60,000',
    '35,000',
    '80,000',
    '450,000',
    '75,000',
  ],
  add_dates: [
    '2021-11-24',
    '2024-01-22',
    '2023-08-15',
    '2022-06-10',
    '2023-04-03',
    '2023-02-05',
    '2022-10-17',
    '2023-12-08',
    '2021-09-30',
    '2022-04-12',
  ],
};

/**
 * 더미 데이터 만들기
 */
function createDummy(n) {
  const dummy = [];
  while (n--) {
    dummy.push(createItem());
  }
  return dummy;
}

function createItem() {
  const item = {};
  item.gender = fashionData.genders[randNum(3)];
  item.category =
    fashionData.categories[randNum(fashionData.categories.length)];
  item.brand = fashionData.brands[randNum(fashionData.brands.length)];
  item.product = fashionData.products[randNum(fashionData.products.length)];
  item.price = fashionData.prices[randNum(fashionData.prices.length)];
  item.add_date = fashionData.add_dates[randNum(fashionData.add_dates.length)];
  return item;
}

function randNum(n) {
  return Math.floor(Math.random() * n);
}

// 테스트용 더미데이터
const originalData = createDummy(101);
let filteredData = [...originalData];

/**
 * 테이블에 추가할 아이템
 */
let checkedCount = 0;
function createNewRowByData(data, index) {
  const row = document.createElement('tr');
  const checkbox = document.createElement('input');
  checkbox.value = index;
  checkbox.type = 'checkbox';
  checkbox.classList.add('form-check-input');

  row.insertCell(0).appendChild(checkbox);
  row.insertCell(1).innerHTML = data.category;
  row.insertCell(2).innerHTML = data.brand;
  row.insertCell(3).innerHTML = data.product;
  row.insertCell(4).innerHTML = data.price;
  row.insertCell(5).innerHTML = data.gender;
  row.insertCell(6).innerHTML = data.add_date;

  checkbox.addEventListener('change', (event) => {
    if (checkbox.checked) {
      row.classList.add('table-primary');
      checkedCount++;
    } else {
      row.classList.remove('table-primary');
      checkedCount--;
    }
    if (!isCheckAllClick) {
      checkAllEl.checked = checkedCount === DISPLAY_NUMBER;
    }
  });

  row.addEventListener('click', (event) => {
    if (event.target === checkbox) return;
    checkbox.click();
  });
  return row;
}

function createEmptyRow() {
  const row = document.createElement('tr');
  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.classList.add('form-check-input');

  row.insertCell(0).innerHTML = '&nbsp';
  row.insertCell(1);
  row.insertCell(2);
  row.insertCell(3);
  row.insertCell(4);
  row.insertCell(5);
  row.insertCell(6);
  return row;
}

/**
 * 전체 선택/해제
 */
checkAllEl.addEventListener('change', (event) => {
  const checkboxes = dataTable.querySelectorAll('input[type=checkbox]');
  isCheckAllClick = true;
  checkboxes.forEach((checkbox) => {
    if (checkbox.checked === event.target.checked) return;

    checkbox.checked = event.target.checked;
    checkbox.dispatchEvent(new Event('change'));
  });
  isCheckAllClick = false;
});

/**
 * 테이블 리셋
 * 데이터 추가, 삭제, 업데이트, 필터 등등...
 */
function resetTable() {
  dataTable.innerHTML = '';
}

/**
 * 테이블에 데이터 전부 출력
 */
function printAllData() {
  printDataByDataSet(originalData);
}

/**
 * 테이블에 데이터 출력(데이터셋 필요)
 */
function printDataByDataSet(dataSet) {
  dataTable.innerHTML = '';
  document.getElementById('check-all').checked = false;
  dataSet.forEach((data, index) => {
    const row = createNewRowByData(data, index);
    dataTable.appendChild(row);
  });
  if (dataSet.length < DISPLAY_NUMBER) {
    const diff = DISPLAY_NUMBER - dataSet.length;
    for (let i = 0; i < diff; i++) {
      dataTable.appendChild(createEmptyRow());
    }
  }
}

// printAllData();

/* pagenation */
const pagenation = document.getElementById('pagenation');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
let pageButtons = [];
let fullPage = 0;
let currentPage = 0;
let startIdx = 0;
let lastIdx = startIdx + DISPLAY_NUMBER;
let currentData = [];
initPagenation();

function initPagenation() {
  startIdx = 0;
  lastIdx = startIdx + DISPLAY_NUMBER;
  fullPage = Math.ceil(filteredData.length / 20) - 1;
  currentPage = 0;
  currentData = filteredData.slice(startIdx, lastIdx);
  createPageButtons();
  printDataByDataSet(currentData);
}

function createPageButtons() {
  pagenation.innerHTML = '';
  pagenation.appendChild(prevBtn);
  pageButtons = [];
  for (let i = 0; i <= fullPage; i++) {
    const pageBtn = createPageButton(i);
    pageButtons.push(pageBtn);
    pagenation.appendChild(pageBtn);
  }
  console.log(pageButtons);
  pagenation.appendChild(nextBtn);

  prevBtn.classList.add('disabled');
}

function createPageButton(pageNum) {
  const li = document.createElement('li');
  li.classList.add('page-item');
  if (pageNum === 0) li.classList.add('active');

  const a = document.createElement('a');
  a.classList.add('page-link');
  a.setAttribute('href', '#');
  a.innerText = pageNum + 1;
  a.value = pageNum;
  a.addEventListener('click', (event) => {
    event.preventDefault();
    document.activeElement.blur();
    const selectedPage = event.target.value;
    if (selectedPage === currentPage) return;
    changePage(selectedPage);
  });

  li.appendChild(a);
  return li;
}

function changePage(selectedPage) {
  // 버튼이 포커스 되어있으면 보기 이상해서 포커스 해제
  document.activeElement.blur();

  window.scrollTo(0, 0);
  // 페이지를 기준으로 데이터배열에서 가져올 데이터 인덱스 설정
  startIdx = selectedPage * DISPLAY_NUMBER;
  lastIdx = getLastIdx(startIdx);

  // 설정된 인덱스를 기준으로 데이터 추출 및 테이블 출력
  currentData = filteredData.slice(startIdx, lastIdx);
  printDataByDataSet(currentData);

  // 페이지 버튼 active 변경
  pageButtons[currentPage].classList.remove('active');
  pageButtons[selectedPage].classList.add('active');
  currentPage = selectedPage;

  // prev, next 버튼 active 설정
  if (currentPage) {
    prevBtn.classList.remove('disabled');
  } else {
    prevBtn.classList.add('disabled');
  }

  if (currentPage < fullPage) {
    nextBtn.classList.remove('disabled');
  } else {
    nextBtn.classList.add('disabled');
  }
}

function setNextPageIdx() {
  startIdx = lastIdx;
  lastIdx += getLastIdx(startIdx);
  console.log(lastIdx);
}

function getLastIdx(startIdx) {
  return startIdx + DISPLAY_NUMBER > filteredData.length
    ? filteredData.length
    : startIdx + DISPLAY_NUMBER;
}

prevBtn.addEventListener('click', () => {
  if (currentPage === 0) return;
  changePage(currentPage - 1);
});

nextBtn.addEventListener('click', () => {
  if (currentPage === fullPage) return;
  changePage(currentPage + 1);
});

/* 필터링 */
/**
 * a에 b가 포함되어 있는지 체크하는 함수
 * @param {string} a
 * @param {string | string[]} b
 * @returns {boolean}
 */
function checkInclude(a, b) {
  if (typeof b === 'string') {
    return a.toLowerCase().includes(b.toLowerCase());
  } else {
    a = a.toLowerCase();
    return b.some((_b) => a.includes(_b.toLowerCase()));
  }
}

/**
 * 브랜드와 상품명에 keyword가 포함되어 있는 아이템만 선택
 */
function filterByKeywords(data, keywords) {
  if (!data.length) return [];
  if (keywords[0] === '') return data;
  return data.filter((item) => {
    const brandName = item.brand.split(' ').join('').toLowerCase();
    const productName = item.product.split(' ').join('').toLowerCase();
    return (
      checkInclude(brandName, keywords) || checkInclude(productName, keywords)
    );
  });
}

/**
 *
 * 현재 선택된 카테고리와 일치하는 아이템만 선택
 */
function filterByCategory(data, category) {
  if (!data.length) return [];
  return data.filter((item) => {
    return category === 'all' ? true : item.category === category;
  });
}

function getFilteredData(data, keywords, category) {
  return filterByCategory(filterByKeywords(data, keywords), category);
}

// 조회버튼
const categoryEl = document.getElementById('inlineFormSelectPref');
const searchForm = document.getElementById('search-form');
searchForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const keywords = searchForm.searchInput.value.trim().split(' ');
  const category = categoryEl.value;
  filteredData = getFilteredData(originalData, keywords, category);
  initPagenation();
  console.log(currentPage);
});

// 카테고리 선택
categoryEl.addEventListener('change', (event) => {
  // const selectedCategory = event.target.value;
  // pt.setCategory(selectedCategory);
  // if(selectedCategory === 'all'){
  //   printAllData();
  // }else{
  //   const filteredData = data.filter((item) => item.category === selectedCategory);
  //   printDataByDataSet(filteredData);
  // }
});
