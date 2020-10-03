// https://velog.io/@modolee/jsconf2020-karrot-market-quiz


const obj = {
  title: '자바스크립트',
  subObj: {
    title: 'Javascript',
    show(func) {
      return func.apply(this);
    }
  },
  show() {
    return this.subObj.show(() => {
      // console.log(this.subObj.title)
      return this.title;
    });
  }
}

console.log(obj.show() === '자바스크립트' ? 'O' : 'X');