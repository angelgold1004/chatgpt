graph TB;
    A[요구 사항 분석] --> B[아키텍처 설계]
    B --> C[데이터베이스 설계]
    C --> D[백엔드 개발]
    D --> E[프론트엔드 개발]
    E --> F[인증 및 보안]
    F --> G[결제 처리]
    G --> H[테스팅]
    H --> I[배포 및 유지보수]
    I --> J[확장성 고려]

classDiagram
    class Database {
        -호텔 정보
        -예약 정보
        -사용자 정보
    }

sequenceDiagram
    participant User
    participant System
    participant Hotel
    participant Room
    participant Reservation

    User->>System: 로그인
    activate User
    activate System
    System->>User: 로그인 화면 표시
    User-->>System: 로그인 정보 입력
    System-->>User: 로그인 성공

    User->>System: 호텔 검색
    System-->>User: 호텔 목록 표시

    User->>System: 호텔 선택
    System-->>User: 객실 목록 표시

    User->>System: 객실 선택
    System-->>User: 예약 정보 입력 화면 표시

    User->>System: 예약 정보 입력
    System-->>User: 결제 화면 표시

    User->>System: 결제
    System->>Hotel: 객실 예약 상태 변경 요청
    activate Hotel
    Hotel-->>System: 객실 예약 상태 변경 완료
    deactivate Hotel
    System-->>User: 예약 완료

    User->>System: 로그아웃
    System-->>User: 로그아웃 성공
    deactivate System
    deactivate User
