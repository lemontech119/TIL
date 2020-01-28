#### HTTP 통신

- Client의 요청(Request)이 있을 때만 서버가 응답(Request)하여 해당 정보를 전송하고 곧바로 연결을 종료하는 방식
- Client가 요청을 보내는 경우에만 Server가 응답하는 단방향적 통신
- 일반적으로 Server가 Client로 요청을 보낼수는 없습니다.
- 필요한 경우에만 Server로 접근하는 콘텐츠 위주의 데이터를 사용할 때만 용이함



#### Socket 통신

- Server와 Client가 특정 Port를 통해 실시간으로 양방향 통신을 하는 방식
- Server역시 Client로 요청을 보낼 수 있습니다.
- 실시간 통신이 필요한 경우에 자주 사용
  - 동영상 스트리밍 서비스, 채팅 서비스 등