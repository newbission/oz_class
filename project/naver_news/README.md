# NAVER OPINION
> 네이버 뉴스의 오피니언을 분류별로 수집
>
> url: `https://news.naver.com/opinion/series?whole=Y&sid=`  
> category: `["NORMAL", "POLITICS", "ECONOMY", "SOCIETY", "LIFE", "WORLD", "IT"]`

### 수집정보
> [!IMPORTANT]
> **title**: 기사 제목  
> **press**: 언론사
> **journalist**: 기자(없는 경우도 있어서 `NULL` 가능)  
> **upload_time**: 최초 업로드 날짜 및 시각  
> **update_time**: 마지막으로 수정된 날짜 및 시각  
> **naver_url**: 네이버 주소  
> **original_url**: 원문 주소  
> **summary**: 기사 상단 요약 
> **header**: 기사 주제
> **thumbnail_url**: 썸네일 원본 url
> **thumbnail_file_name**: 썸네일 저장본 이름
> **category**: 기사 카테고리


```SQL
CREATE TABLE naver_opinion(
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  press VARCHAR(20) NOT NULL,
  journalist VARCHAR(5),
  upload_time TIMESTAMP NOT NULL,
  update_time TIMESTAMP DEFAULT NULL,
  naver_url VARCHAR(255) NOT NULL,
  original_url VARCHAR(255),
  summary VARCHAR(255),
  header VARCHAR(20),
  thumbnail_url VARCHAR(255),
  thumbnail_file_name VARCHAR(20),
  category VARCHAR(5)
)
```
