const form = document.getElementById('form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const target = event.target;
  const userId = target.id.value;
  const userPw1 = target.pw1.value;
  const userPw2 = target.pw2.value;
  const userName = target.name.value;
  const userPhone = target.phone.value;
  const userPosition = target.position.value;
  const userGender = target.gender.value;
  const userEmail = target.email.value;
  const userIntro = target.intro.value;

  if(userId.length < 6) {
    alert('아이디는 최소 6글자 이상입니다!!');
    return;
  }

  if(userPw1 !== userPw2) {
    alert('비밀번호가 일치하지 않습니다!!');
    return;
  }
  
  document.body.innerHTML = '';
  document.write(`
    <h1>${userId}님 확연합니다</h1>
    회원 가입 시 입력하신 내역은 다음과 같습니다.
    <ul>
      <li>아이디 : ${userId}</li>
      <li>이름 : ${userName}</li>
      <li>전화번호 : ${userPhone}</li>
      <li>원하는 직무 : ${userPosition}</li>
      <li>성별 : ${userGender}</li>
      <li>이메일 : ${userEmail}</li>
      <li>자기소개 : ${userIntro}</li>
    </ul>
  `)
})