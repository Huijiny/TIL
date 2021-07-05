# Github page에 자동 배포화(DevOps)	

서울 4반 유희진



<img src="https://images.velog.io/images/huijiny/post/361855fc-e32a-46d9-ad25-75b838cdd78a/image.png" alt="drawing" width="300"/>

# 🌱 개요

프로젝트에서 일련의 과정을 보자면 절대 코드를 개발하는 단계 하나로 이루어져 있지 않다. 기획하고, 기획에 따라 와이어프레임을 짜거나 DB 구조를 짜는 등의 설계를 한 다음, 개발이 진행된다. 개발이 끝났다고 해서 프로젝트가 끝났다고 할 수 없다. 프로젝트에 테스트 코드를 입혀 이 프로젝트가 각각의 유닛 테스트에서 제대로 작동하는지를 확인 후 배포 단계에 거친다. 배포가 끝났다고 하여 바로 상용단계가 아닌, 알파 및 베타 테스트 등을 거친 뒤에야 상용 단계에 이른다. 

이 일련의 과정을 모두 끝내 사용자가 그 프로젝트의 산출물을 사용할 단계에 도달하여 개발자와의 꾸준한 피드백을 통해 그 산출물을 유지보수 하는 상황까지 가야 프로젝트가 마무리 단계에 이르렀다고 생각한다.



## 💛 DevOps란? 
> 데브옵스(DevOps)는 소프트웨어의 개발(Development)과 운영(Operations)의 합성어로서, 소프트웨어 개발자와 정보기술 전문가 간의 소통, 협업 및 통합을 강조하는 개발 환경이나 문화를 말한다. 데브옵스는 소프트웨어 개발조직과 운영조직간의 상호 의존적 대응이며 조직이 소프트웨어 제품과 서비스를 빠른 시간에 개발 및 배포하는 것을 목적으로 한다. 
> _from wiki백과_



**오늘은 vue.js를 통해 간단하게 프로젝트를 생성하고, github pages에 수동배포를 한 후 , actions workflow로 배포 자동화를 연습해보고자 한다.**

---





# ❗️START

## 2.1 Vue 프로젝트 생성 및 로컬 실행 확인
vue 프로젝트를 만든다.
vue 프로젝트 만드는 법은 [Vue-CLI-router 포스트](https://velog.io/@huijiny/Vue-CLI-router) 를 보면 나온다. 
나는 아래와 같이 명렁어를 쳤다. 

``` 
vue create huijin-page
```
![](https://images.velog.io/images/huijiny/post/4161f315-e70f-4602-abd8-f12329c378da/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-29%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.09.25.png)
위에서 얘기했듯, huijin-page로 만들어봤다! 나는 무지폴더를 하나 만들어서 그 위에서 만들었고, `cd` 명렁어를 통해서 huijin-page를 들어간다음 `npm run serve`를 통해서 확인해보면,
![](https://images.velog.io/images/huijiny/post/285ed300-f9e7-407a-aec3-0a6b00895043/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-29%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.12.15.png)
이렇게 프로젝트 생성이 깔끔하게 완료되었고, 실행도 완료되었다.
오류가 있으면 이 과정에서 멈추고 오류를 뱉는다.
![](https://images.velog.io/images/huijiny/post/1e0e1c34-c4a2-486d-bc28-cf607ab8e09a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-29%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.14.35.png)
이렇게 만든 뷰 프로젝트를 일단 내부 코드를 고치지 않고 github page에 수동배포를 해봐야겠다.
![](https://images.velog.io/images/huijiny/post/2f6fcea7-a3a3-496a-8658-f335a368aaf8/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-29%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.13.59.png)

## 2.2 GitHub에 코드 Push 및 Pages에 수동 배포

### 1. Github에 레포지토리 생성
깃헙에 레포지토리를 하나 판다. 나는 이름을 맞춰서 huijin-page로 ..!
![](https://images.velog.io/images/huijiny/post/6dc88694-dcbf-4447-a295-491bf8b5bba4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-29%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.18.17.png)

### 2. 원격 저장소 설정 및 코드 푸시
로컬 vue 프로젝트에 origin을 추가해주고, 프로젝트 생성할 때 만들어진 첫 커밋을 push 해준다.
```
git remote add origin [repository 주소]
git push -u origin master
```
### 3. github pages로 배포하기 위해 라이브러리를 추가, package.json에 배포에 필요한 정보 추가

![](https://images.velog.io/images/huijiny/post/589e01c2-967f-4e41-8362-6f0fa46f3e36/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-29%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.20.34.png)
나는 `yarn`이 깔려있지 않아서 `npm`으로 그냥 진행했다.
![](https://images.velog.io/images/huijiny/post/71ed3777-4c60-4870-8ace-c0bd63e1d6a0/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-29%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.22.21.png)

package.json에 homepage, script > predeploy, deploy, clean 부분 추가
![](https://images.velog.io/images/huijiny/post/733ae79a-3738-44b1-9f06-432788cc0de4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-29%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.24.48.png)
### 4. 배포용 publicPath 설정
![](https://images.velog.io/images/huijiny/post/3997c40a-2735-49ef-b40c-60c56371c867/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-29%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.26.25.png)
이 설정이 있어야지 깃헙 page에서 정상적으로 페이지 확인이 가능하다고 한다.
프로젝트 최 상단에 `vue.config.js`파일을 생성하고, publicPath에 생성한 repository 이름으로 설정한다.

만약 huijin-page 대신 <github_id>.github.io 이런 주소를 Github Pages 대표 주소로 사용하고자하면 이 설정은 굳이 할 필요가 없고, 접속할 주소도 `https://<github_id>.github.io` 이렇게 사용이 가능하다. 나는 일단 뒤에 huijin-page를 붙여줬다!

### 5. npm run deploy


![](https://images.velog.io/images/huijiny/post/b61302cc-6259-4346-ab31-e70182302ab6/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-29%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.34.49.png)
`npm run deploy` 명령을 통해 빌드된 정적파일을 원격 저장소의 `gh-pages` 브랜치를 알아서 생성해서 푸쉬한다고 한다. 
이곳에서 만약 이 이 에러가 등장한다면 yarn clean을 하고 재시도 하라고 한다.

```
fatal: A branch named 'gh-pages' already exists.
error Command failed with exit code 1
```

### 6. 설정에서 배포된 주소를 확인, 및 접속

![](https://images.velog.io/images/huijiny/post/4728fbfb-eb5b-4010-ace0-84b9428063ee/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-29%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.35.45.png)
형광 초록 색 부분에 링크를 들어가보 면 아래와 같이 배포된 화면이 나온다!!! 
주목할 부분은 링크! 링크가 아까 설정해놓은 것과 같이 <github_id>.github.io/project-name/이라는 걸 볼 수 있다. 
![](https://images.velog.io/images/huijiny/post/7e4a84b1-e75d-4353-84d0-6604d612a4db/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-06-29%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.36.07.png)
## 2.3 GitHub Actions workflow로 배포 자동화
github은 원격 git 저장소로 코드를 호스팅하는 서비스로 출발했지만 지금은 개발자와 DevOps 엔지니어 팀이 신속하게 애플리케이션을 빌드하고 배포할 수 있도록 지원하고 있다고 한다. 
Github Actions는 github의 소프트웨어 개발 워크플로에서 작업을 자동화하기 위한 패키지 스크립트다. 개잘자가 새 소스 코드를 Push / PR 같은 이벤트에 반응해 트리거하도록 구성할 수 있다고 한다.

아래에서는 이 기능을 사용해 Vue로 작성된 소스코드를 자동으로 테스트하고, 빌드하여 자동으로 pages에 배포하는 것을 해본다.

### 1. Github Actions 메뉴의 첫 화면에서 보여주는 Simple workflow (deploy.yml)을 작성한다음 커밋한다.
![](https://images.velog.io/images/huijiny/post/b7bfbfb1-408f-418f-8447-5ee833179790/13.png)
여기서 저 `Set up this workflow` 버튼을 누르고,
![](https://images.velog.io/images/huijiny/post/762bfcbf-345b-462b-aabc-c14ec8cce6d5/14.png)
이름을 `deploy.yml`으로 바꾸고,
![](https://images.velog.io/images/huijiny/post/3f60829a-d681-45eb-a029-4420a752b923/15.png)
커서가 파란색으로 칠해진 부분을 `Deployment`로 바꾼다.

### 2. 커밋과 동시에 샘플 workflow가 동작되는 것을 확인한다.
![](https://images.velog.io/images/huijiny/post/11b4585b-6098-4452-b1bc-dda99cf5f870/16.png)
![](https://images.velog.io/images/huijiny/post/01147a46-093c-4894-a730-c4afc249ab2c/17.png)
옆에 start commit 버튼을 누르고 커밋을 한 뒤, actions 탭에 가면 방금 커밋한 워크플로우가 진행되고 있다. 

### 3. 로컬에서 진행

![](https://images.velog.io/images/huijiny/post/78d21bea-19b4-4eb0-840e-e18428c8e82c/18.png)
`git pull` 명령어를 사용해 방금 리모트(깃헙)에서 커밋한 작성 사항을 내려받는다.
그러면 숨김폴더중에 `.github/workflow `가 있는데, 이걸 찾느라 한참걸렸다.
여기서 `deploy.yml` 파일을 수정할 것.

### 4. deploy.yml 파일 수정

_**참고**_
1. 나는 npm을 사용했다. 
2. 여기서 헷갈렸던 부분이 맨 아래 github_token에 personal access token을 넣는 줄 알았는데, 아니고 그대로 넣으면 기존에 내부에 저장되어있는 GITHUB_TOKEN이라는 토큰이랑 매칭되는 듯 하다.

``` yml
# This is a basic workflow to help you get started with Actions

name: Deployment

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the master branch
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  deploy:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      - name: Checkout source code
        uses: actions/checkout@master

      - name: Set up Node.js
        uses: actions/setup-node@master
        with:
          node-version: 14.17.1

      - name: Install dependencies
        run: npm install

      - name: Build page
        run: npm build
        env:
          NODE_ENV: production

      - name: Deploy to gh-pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist

```
각각의 명령어의 의미는 아래 reference에 추가해놓은 블로그에서 아주 잘 설명해주고 있어서 추가해놓았다. 
### 5. HellowWord로 내리는 props를 `heejin page`로 바꿨다. 
![](https://images.velog.io/images/huijiny/post/b87a505d-56e0-4bb7-96f8-66c0131de121/19.png)
### 6. push
![](https://images.velog.io/images/huijiny/post/3b4853a4-8557-474b-8302-be0949410c28/20.png)

### 7. Action 탭에서 확인
사진이 이것 밖에 없는데, 잘 돌고 배포가 되었다.
보면 노란색은 현재 배포 진행중
빨간색은 배포 실패
초록색은 배포 성공을 뜻한다.

나는 npm을 사용해서 npm run build를 했었어야했는데 yarn 처럼 npm build를 해놔서... 실패했다. 한참찾았다...!

![](https://images.velog.io/images/huijiny/post/af853887-bb1d-4a5c-bc6d-59289a01e529/21.png)
## 2.4 코드 수정 및 테스트 실패로 인한 자동 배포 실패 확인

자동으로 저렇게 배포되는게 너무 편리하고 좋지만, 만약 확인되지 않은 코드가 그대로 배포된다면 사용자들에게 큰 불편을 줄 수 있다.
그렇기 때문에 테스트가 꼭 필요하다.
사실 나는 테스트 코드 개발은 학부생 때 소프트웨어 공학 시간에 배웠던 것 밖에 없어서ㅠ 모른다고 말할 수 있다.
여기서는 yml 파일에 npm 테스트 명령을 통해서 테스트 해보려고 한다.
하지만, 본래는 테스트 코드를 직접 짜는 게 좋다!

### 1. 유닛 테스트 코드 추가
![](https://images.velog.io/images/huijiny/post/728f42b6-e088-4e62-a658-1403eb217a52/22.png)
### 2. helloworld에서 msg props 받지않기
![](https://images.velog.io/images/huijiny/post/b5503d07-6b79-45d3-af16-acca650d9b7b/23.png)
### 3. 진행중
![](https://images.velog.io/images/huijiny/post/73cb77e6-47f2-40c9-b36b-ddb5c98a900b/24.png)
### 4. 실패!
![](https://images.velog.io/images/huijiny/post/a50606a5-d804-4090-80a2-e191e8f6d91b/25.png)

## 2.5 코드 재 수정 및 배포 성공 확인
코드를 다시 전으로 수정하고, 성공한 코드를 배포한다.
### 1. 코드 수정
![](https://images.velog.io/images/huijiny/post/7c5b3dba-6ef2-4d92-a795-b4416c5f5797/26.png)
### 2. 성공한 화면 :)
![](https://images.velog.io/images/huijiny/post/664c8e24-a508-420b-8bd8-4b8b161a8839/27.png)
### This is Huijin Page >_<
얼른 잘 꾸밀 날이 오기를..
![](https://images.velog.io/images/huijiny/post/289c24df-7104-435a-8b23-60d2a59d55cd/28.png)

## 끝으로

동아리를 하면서 다른 팀원이 자기 CI 붙여놨으니 확인해보라고 했을 때 이해를 못했던 경험이 기억난다 ^^



## Reference

https://velog.io/@gwak2837/GitHub-Pages-gh-pages%EB%A1%9C-%EB%AC%B4%EB%A3%8C-%EC%9B%B9-%ED%98%B8%EC%8A%A4%ED%8C%85%ED%95%98%EA%B8%B0

https://velog.io/@kimdoyeong/Github-Actions%EB%A1%9C-Github-Pages-%EC%9E%90%EB%8F%99-%EB%B0%B0%ED%8F%AC