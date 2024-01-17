/* 계산기 */
function calculator() {
  const display = document.querySelector('.calc_display');
  const btns = document.querySelectorAll('.calc_btns > button');
  let currentOp = '';
  let currentNum = '0';
  let preNum = '';
  btns.forEach((btn) => {
    btn.addEventListener('click', btnClickHandler);
  });
  function init() {
    result = 0;
    preNum = '';
    display.innerText = '0';
    currentOp = '';
    currentNum = '0';
  }

  function btnClickHandler(event) {
    const value = event.target.value;
    if (value === 'C') {
      init();
      return;
    }
    if (isOp(value)) {
      if (currentNum.length) {
        preNum = currentNum;
        currentNum = '';
      }
      currentOp = value;
    } else if (value === '=') {
      if (
        preNum.length === 0 ||
        currentOp.length === 0 ||
        currentNum.length === 0
      ) {
        return;
      }
      preNum = calc(+preNum, +currentNum, currentOp) + '';
      currentNum = '';
      currentOp = '';
    } else {
      if(preNum.length && currentOp.length === 0) {
        preNum = '';
      }
      if (currentNum.length === 1 && currentNum[0] === '0') {
        currentNum = value;
      } else {
        currentNum += value;
      }
    }
    display.innerText = `${preNum} ${currentOp} ${currentNum}`
  }

  function isOp(c) {
    switch (c) {
      case '+':
      case '-':
      case 'X':
      case '÷':
        return true;
      default:
        return false;
    }
  }

  function calc(a, b, op) {
    switch (op) {
      case '+':
        return a + b;
      case '-':
        return a - b;
      case 'X':
        return a * b;
      case '÷':
        return a / b;
    }
  }

  init();
}

calculator();


function gugudan() {
  const tr = document.querySelector('.gugu_table');
  for(let i=2; i<=9; i++){
    const td = document.createElement('td');
    for(let j=1; j<=9; j++){
      const p = document.createElement('p');
      p.innerText = `${i} X ${j} = ${i*j}`;
      td.append(p);
    }
    tr.append(td);
  }
}

gugudan();

function time() {
  const div = document.querySelector('.time_wrap');
  
  setInterval(() => {
    const now = new Date();
    const diff = getDiff(now);
    div.innerHTML = 
    `현재 시각: ${now}<br>
    올해의 남은 시간: ${diff}
    `;
  }, 1000);

  function getDiff(d1) {
    const d2 = new Date('2024-12-31 23:59:59:999');
    const diff = d2.getTime() - d1.getTime();
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hour = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const min = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const sec = Math.floor((diff % (1000 * 60)) / 1000);
    return `${days}일 ${hour}시간 ${min}분 ${sec}초`;
  }
}

time();

function Stopwatch() {
  const display = document.querySelector('.sw_display');
  const startBtn = document.querySelector('.sw_start');
  const stopBtn = document.querySelector('.sw_stop');

  let startTime = 0;
  let stopTime = 0;
  let isRun = false;

  let timer = null;

  function start(){
    if(isRun) return;
    stopBtn.innerText = '정지';
    isRun = true;
    startTime = new Date() - Math.abs(stopTime - startTime);
    timer = setInterval(() => {
      const now = new Date();
      const diff = now - startTime;
      changeDisplay(diff);
    }, 10);
  }

  function stop(){
    const type = stopBtn.innerText;
    if(type === '정지'){
      stopBtn.innerText = '리셋'
      clearInterval(timer);
      isRun = false;
      stopTime = new Date();
    }else {
      stopBtn.innerText = '정지'
      reset();
    }
  }
  function reset(){
    startTime = 0;
    stopTime = 0;
    isRun = 0;
    display.innerText = `경과 시간: 0:0:0`
  }

  function changeDisplay(time) {
    const m = Math.floor(time / (1000 * 60));
    const s = Math.floor(time / 1000);
    const ms = Math.floor((time % 1000));
    
    display.innerText = `경과시간: ${m}:${s}:${ms}`;
  }
  reset();
  startBtn.addEventListener('click', start);
  stopBtn.addEventListener('click', stop);
}

Stopwatch();