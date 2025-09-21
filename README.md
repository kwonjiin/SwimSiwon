# 🏊 SwimTalk

AI 기반 수영일지 관리 & 진도 관리 챗봇 시스템입니다.\
React + FastAPI + OpenAI GPT API + Redis + MariaDB 로 구성되었습니다.

------------------------------------------------------------------------

## 🚀 주요 기능

-   수영 토크 챗봇 (OpenAI GPT API 기반)
-   수영일지 작성 및 저장 (MariaDB)
-   진도 관리 및 통계 제공
-   JWT 인증 기반 로그인/회원가입
-   SSE/Redis 기반 알림 기능

------------------------------------------------------------------------

## 🛠 기술 스택

-   **Frontend**: React, TailwindCSS
-   **Backend**: Python (FastAPI)
-   **AI**: OpenAI GPT API
-   **Database**: MariaDB
-   **Cache & Pub/Sub**: Redis
-   **Auth**: JWT (JSON Web Token)
-   **Infra**: Docker, Nginx

------------------------------------------------------------------------

## 📂 프로젝트 구조

    📦 swimming-talk-chatbot
    ├── 📂 frontend          # React 앱 (챗봇 UI, 수영일지 UI)
    ├── 📂 backend           # FastAPI 서버 (API, JWT 인증, DB 연결)
    │   ├── app
    │   │   ├── auth         # 로그인/회원가입, JWT 인증
    │   │   ├── models       # SQLAlchemy 모델 (User, Diary, Progress)
    │   │   ├── routes       # API 라우터
    │   │   ├── services     # 비즈니스 로직
    │   │   ├── db           # DB 세션/연결
    │   │   └── main.py      # FastAPI 진입점
    ├── 📂 docs              # 문서, ERD 다이어그램 등
    ├── docker-compose.yml
    └── README.md

------------------------------------------------------------------------

## ⚙️ 실행 방법

### 1️⃣ 백엔드 실행 (FastAPI)

``` bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 2️⃣ 프론트엔드 실행 (React)

``` bash
cd frontend
npm install
npm start
```

### 3️⃣ Docker 실행 (전체 서비스)

``` bash
docker-compose up --build
```

------------------------------------------------------------------------

## 🗄 데이터베이스 ERD

-   **User**: id, email, password, nickname
-   **Diary**: id, user_id, date, content
-   **Progress**: id, user_id, skill, level, notes

------------------------------------------------------------------------

## 🔒 인증 (JWT)

-   `/auth/signup` → 회원가입
-   `/auth/login` → 로그인 후 JWT 발급
-   `/users/me` → 현재 로그인된 유저 정보 확인

요청 시 `Authorization: Bearer <token>` 필요

------------------------------------------------------------------------

## 📌 TODO

-   [ ] 수영일지 검색 기능
-   [ ] 진도 자동 분석 AI 기능
-   [ ] 모바일 앱 대응 (React Native)

------------------------------------------------------------------------