# chatgpt
classDiagram
    class User {
        +ID: int
        +이름: string
        +이메일: string
        +비밀번호: string
        +로그인()
        +회원가입()
        +예약하기()
        +예약취소()
    }

    class Hotel {
        +ID: int
        +이름: string
        +주소: string
        +별점: float
        +가격: int
        +객실목록: Room[]
        +예약목록: Reservation[]
        +호텔정보조회()
        +예약하기()
        +예약취소()
    }

    class Room {
        +ID: int
        +호텔ID: int
        +종류: string
        +가격: int
        +예약가능여부: bool
        +예약정보: Reservation[]
        +예약하기()
        +예약취소()
    }

    class Reservation {
        +ID: int
        +사용자ID: int
        +객실ID: int
        +체크인날짜: date
        +체크아웃날짜: date
        +예약상태: string
        +예약정보조회()
        +예약취소()
    }

    User --> Reservation: 예약
    Hotel --> Room: 포함
    Hotel --> Reservation: 예약
    Room --> Reservation: 예약
