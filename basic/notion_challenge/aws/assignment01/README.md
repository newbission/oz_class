# 클라우드

## 클라우드 컴퓨팅
> [!NOTE]
>  **클라우드 컴퓨팅**은 줄여서 클라우드라고도 부르며 구름속에 리소스(서버, 스토리지, 데이터베이스 등의 전산자원)들을 넣어놓고 시간과 장소에 구애받지 않고 구름속에 있는 리소스들을 사용할 수 있도록 하는 개념이다.  

> 인터넷을 통해서 바로 사용 가능하며 사용한 만큼만 비용을 지불하면 되기 때문에 초기에 들어가는 비용이 줄어든다는 장점이 있다.  
> 대부분의 스타트업에서 사용하며 빠르게 인프라를 구축하고 비즈니스에만 집중할 수 있어 빠르게 사업을 진행할 수 있는 장점이 있다.  
> 하지만 기업의 비즈니스 목적에 알맞는 클라우드를 선정하지 못한다면 배보다 배꼽이 더 커져 많은 비용을 지불해야 할 수도 있다.

## 클라우드의 종류
> [!NOTE]  
> 클라우드의 종류에는 IaaS, PaaS, SaaS가 있다.

![pizza as a service](https://media.licdn.com/dms/image/C4E12AQH3p44mG-q4Wg/article-inline_image-shrink_1000_1488/0/1520041067201?e=1714003200&v=beta&t=4L79WDcnZ6eUlSv1XdQNL_uyKhNT2iPcwsY52d15tB8)

### On-Premise
> 온프레미스(On-Premise) 방식은 클라우드 서비스를 사용하지 않고 직접 서버를 운영하는 방식이다.  
> 다음은 온프레미스가 클라우드와 다른 이유를 GPT가 설명한 것이다.
> ```
> 온프레미스 방식으로 운영되는 서버를 사용하더라도, 사내 조직원이 어디서든 접근할 수 있는 경우를 클라우드 방식으로 운영되는 것으로 간주하기는 어렵습니다. 이는 온프레미스와 클라우드 간의 주요 차이 중 하나인 리소스 위치와 관리 방식에서의 차이 때문입니다.
> 
> 클라우드 방식은 서버 및 기타 리소스가 인터넷을 통해 외부 공급업체에 의해 호스팅되고 관리된다는 것을 의미합니다. 따라서 사용자는 인터넷을 통해 언제 어디서든지 이 리소스에 접근할 수 있습니다. 또한 클라우드 서비스 제공업체는 자원을 유연하게 확장하거나 축소하여 필요에 따라 지불할 수 있도록 해줍니다.
> 
> 반면 온프레미스 방식은 기업이 자체 데이터 센터나 서버를 보유하고 관리하는 것을 의미합니다. 따라서 이러한 서버에 접근하려면 일반적으로 기업 네트워크에 직접 연결되어야 합니다. 사내 조직원이 어디서든 접근하려면 VPN(Virtual Private Network) 등을 통해 기업 네트워크에 연결해야 할 것입니다. 이 경우에도 사내 네트워크 및 보안 정책 등을 준수해야 하며, 클라우드와는 다른 관리 및 보안 요구사항이 있을 수 있습니다.
> 
> 따라서 온프레미스 방식으로 서버를 운영하더라도 사내 조직원이 어디서든 접근할 수 있게 만들려면 추가적인 네트워크 및 보안 인프라를 구축하고 관리해야 합니다. 이는 클라우드와는 다른 방식의 운영이며, 일반적으로 클라우드 방식으로 운영되는 것으로 보기는 어렵습니다.
> ```
> 온프레미스 방식은 초기 구축비용 뿐만아니라 유지보수 등 신경써야 할 부분이 많다.

### IaaS
> IaaS(Instructure as a Service)  
> 그림에서 냉동 피자로 분류되는 부분으로 재료만 준비되어 있으므로 그 외에 필요한 식기나 조리도구 등을 직접 준비하고 요리하는 과정이 필요하다.
> IaaS는 냉동피자처럼 재료는 준비되어있지만 사용자가 원하는 환경을 직접 구축하고 유지보수 해야하는 등 신경써야 할 부분이 많다.  
> 대표적인 서비스로 Google Cloud Platform(GCP), Amazon Web Service(AWS) 등이 있다.

### PaaS
> Paas(Platform as a Service)  
> 그림에서 배달 피자로 분류되는 부분으로 피자가 만들어져서 오기 때문에 조리를 할 필요가 없어 조리도구와 조리과정은 생략되지만 여전히 피자를 먹기위한 식탁과 같이 먹으면 좋은 음료수를 준비해야 하는 번거로움이 존재한다.  
> PaaS는 개발자들을 위한 클라우드 서비스로 코드를 실행, 테스트, 배포를 할 수 있도록 플랫폼을 제공한다.  
> 개발자는 PaaS 플랫폼을 사용함으로써 오로지 개발에만 집중할 수 있다.
> 대표적인 서비스로 Microsoft Azure App Service, Google App Engine 등이 있다.

### SaaS
> SaaS(Software as a Service)  
> 그림에서 음식점 피자로 분류되는 부분으로 피자부터 식기류, 식탁, 음료까지 모든 피자와 관련된 서비스를 제공받을 수 있기 때문에 사용자는 다른곳에 신경 쓸 필요 없이 돈만 준비하면 된다.  
> SaaS는 개발자뿐만 아니라 소프트웨어를 사용하는 모든 사용자를 위한 서비스로 사용자는 따로 소프트웨어를 설치할 필요없이 웹브라우저만 있다면 어디서든 접근하여 애플리케이션을 사용할 수 있다.  
> 대표적인 서비스로 Naver MyBox, Dropbox, Googld Workspace(G Suite) 등이 있다.

> [!TIP]
> AWS는 IaaS, PaaS, SaaS 모두 제공한다.

# AWS
### 리전(Region)
> 리전은 AWS가 전 세계에서 데이터 센터를 클러스터링 하는 물리적 위치이며 논리적인 데이터 센터 그룹인 가용 영역(AZ)으로 이루어져 있다.  
> 각 AWS 리전은 지리적 영역 내에서 격리되고 물리적으로 분리된 최소 3개의 AZ로 구성된다.  
> 리전은 서로 격리되어 있으며 여러 지역에 위치해있기 때문에 자신이 서비스하는 위치와 최대한 가까운 리전에 서비스를 연결하는 것이 좋다.  
> 한국은 ap-northeast-2	아시아 태평양(서울) 리전을 사용하면 된다.

### 가용 영역(Availability Zone, AZ)
> 리전내에 위치함 데이터 센터 그룹으로 각 가용 영역은 서로 격리되어있어 하나의 가용영역에 문제가 생겨도 다른 가용 영역은 영향을 받지 않는다. 따라서 한 개의 가용역역을 사용하는 것 보다 여러개의 가용 영역을 사용하는 것이 장애로부터 안전할 수 있다.

### 엣지 로케이션(Edge Location)
> 엣지 로케이션은 전세계에 데이터를 빠르게 전송하기 위해 전세계 곳곳에 촘촘하게 배치된 캐시 서버가 운영되는 데이터 센터이다.