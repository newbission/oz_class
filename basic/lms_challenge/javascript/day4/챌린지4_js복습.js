function RPS() {
  const btn = document.getElementById('rps_btn');
  const result = document.getElementById('rps_result');
  const computerImg = document.getElementById('rps_computer_choice');

  const computerRpsImageUrls = [
    'img/rps/rps_computer_rock.png',
    'img/rps/rps_computer_paper.png',
    'img/rps/rps_computer_scissors.png',
  ];

  const userChoices = document.querySelectorAll(
    'input[name="rps_user_choice"]'
  );

  function getUserChoice() {
    for (const choice of userChoices) {
      if (choice.checked) {
        return +choice.value;
      }
    }
  }

  const getComputerResult = () => {
    return Math.floor(Math.random() * 3);
  };

  let winningStreek = 0;
  let losingStreak = 0;
  let watingForResult = false;
  btn.addEventListener('click', () => {
    if (watingForResult) return;

    let computerResult = 0;
    const userChoice = getUserChoice();
    let cnt = 0;
    const changing = setInterval(() => {
      watingForResult = true;
      changeImage(cnt);
      cnt = (cnt + 1) % 3;
    }, 30);
    setTimeout(() => {
      clearInterval(changing);
      computerResult = getComputerResult();
      changeImage(computerResult);

      let res = '';
      // 0:바위 1:보자기 2:가위
      if (computerResult === userChoice) {
        res = '무승부';
        winningStreek = 0;
        losingStreak = 0;
      } else if (userChoice === 2 && computerResult === 0) {
        res = '패배';
      } else if (userChoice === 0 && computerResult === 2) {
        res = '승리';
      } else {
        res = userChoice > computerResult ? '승리' : '패배';
      }

      if (res == '승리') {
        winningStreek++;
        losingStreak = 0;
      } else if (res === '패배') {
        winningStreek = 0;
        losingStreak++;
      }

      result.innerText = `결과: ${res}`;
      if (winningStreek || losingStreak) {
        result.innerText +=
          ' | ' +
          (winningStreek ? `${winningStreek}연승` : `${losingStreak} 연패`);
      }
      watingForResult = false;
    }, 700);
  });

  // 이미지 전환
  function changeImage(cnt) {
    computerImg.setAttribute('src', computerRpsImageUrls[cnt]);
    computerImg.style.width = '100px';
    computerImg.style.height = 'auto';
  }
}

RPS();

function BG() {
  const div = document.getElementById('bg_div');
  const btn = document.getElementById('bg_btn');

  const basicImgUrl = 'img/bg/meme';
  let interval = null;
  let cnt = 1;
  const MAX_CNT = 6;
  btn.addEventListener('click', (event) => {
    const target = event.target;
    if (target.innerText === '실행') {
      target.innerText = '멈춰';
      interval = setInterval(() => {
        console.log(cnt);
        div.style.backgroundImage = `url(${basicImgUrl}${cnt}.jpg)`;
        cnt = (cnt++ % MAX_CNT) + 1;
      }, 50);
    } else {
      target.innerText = '실행';
      clearInterval(interval);
    }
  });
}

BG();

function IceCream() {
  const btnAdd = document.getElementById('icecream_btn_add');
  const btnShow = document.getElementById('icecream_btn_show');
  const btnList = document.getElementById('icecream_btn_list');
  const pList = document.getElementById('icecream_list');

  const icecreamList = [];
  btnAdd.addEventListener('click', () => {
    const input = window.prompt('추가할 아이스크림 이름을 입력하세요. (중복은 자동으로 입력제외됩니다.)');
    console.log(input);
    if(icecreamList.includes(input)) return;
    icecreamList.push(input);
  })

  btnShow.addEventListener('click', () => {
    icecreamList.forEach((icecream) => {
      window.alert(icecream);
    })
  })
  
  btnList.addEventListener('click', () => {
    pList.innerText = icecreamList.join(' ')
  })
}

IceCream();
