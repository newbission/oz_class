// DOM
const dataTable = document.getElementById('data-table');

/**
 * 필수정보
 *
 * 카테고리, 브랜드, 상품명, 가격,  
 * 성별, 등록일자
 */
const data = [
  {
    gender: '공용',
    category: '상의',
    brand: 'Supreme',
    product: '슈프림 박스로고 후드티',
    price: '390,000',
    add_date: '2024-01-15',
  },
  {
    gender: '남자',
    category: '하의',
    brand: 'DIESEL',
    product: '디젤 트랙 팬츠',
    price: '188,000',
    add_date: '2024-01-17',
  },
  {
    gender: '여자',
    category: '신발',
    brand: 'Nike',
    product: '에어포스 1',
    price: '137,000',
    add_date: '2024-01-22',
  },
  {
    gender: '공용',
    category: '패션잡화',
    brand: 'Music&Goods',
    product: '빵빵이 키링',
    price: '29,000',
    add_date: '2024-01-26',
  },
  // ...
];


/**
 * 더미에 들어갈 데이터 내용
 */
const fashionData = {
  genders: ['공용', '남성', '여성'],
  categories: ['상의', '하의', '신발', '모자', '액세서리'],
  brands: ['Nike', 'Adidas', 'Gucci', 'Supreme', 'Zara', 'Puma', 'Converse', 'Fila', 'Balenciaga', 'Vans'],
  products: ['에어포스 1', '트랙 팬츠', '로고 티셔츠', '슬립온 스니커즈', '베이직 모자', '후드 스웨트셔츠', '스키니 진', '버켄스탁 샌들', '체크 무스탕', '구찌 목걸이'], 
  prices: ['390,000', '45,000', '29,000', '120,000', '18,000', '60,000', '35,000', '80,000', '450,000', '75,000'],
  add_dates: ['2021-11-24', '2024-01-22', '2023-08-15', '2022-06-10', '2023-04-03', '2023-02-05', '2022-10-17', '2023-12-08', '2021-09-30', '2022-04-12']
};

/**
 * 더미 데이터 만들기
 */
function createDummy(n){
  const dummy = [];
  while(n--){
    dummy.push(createData());
  }
  return dummy;
}

function createData(){
  const data = {};
  data.gender = fashionData.genders[randNum(3)];
  data.category = fashionData.categories[randNum(fashionData.categories.length)];
  data.brand = fashionData.brands[randNum(fashionData.brands.length)];
  data.product = fashionData.products[randNum(fashionData.products.length)];
  data.price = fashionData.prices[randNum(fashionData.prices.length)];
  data.add_date = fashionData.add_dates[randNum(fashionData.add_dates.length)];
  return data;
}

function randNum(n){
  return Math.floor(Math.random() * n);
}

// 테스트용 더미데이터
const dummy = createDummy(100);
// console.log(dummy);

/**
 * 테이블에 추가할 아이템
 */
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
  row.insertCell(5).innerHTML = data.add_date;

  checkbox.addEventListener('change', (event) => {
    if (checkbox.checked) {
      row.classList.add('table-primary');
    } else {
      row.classList.remove('table-primary');
    }
  });

  row.addEventListener('click', (event) => {
    if (event.target === checkbox) return;
    checkbox.click();
  });
  return row;
}

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
  printDataByDataSet(dummy);
}

/**
 * 테이블에 데이터 출력(데이터셋 필요)
 */
function printDataByDataSet(dataSet) {
  dataSet.forEach((data, index) => {
    const row = createNewRowByData(data, index);
    dataTable.appendChild(row);
  })
}

printAllData();

/**
 * 전체 선택/해제
 */
document.getElementById('check-all').addEventListener('change', (event) => {
  const checkboxes = dataTable.querySelectorAll('input[type=checkbox]');
  checkboxes.forEach(checkbox => {
    checkbox.checked = event.target.checked;
    checkbox.dispatchEvent(new Event('change'));
  })
})