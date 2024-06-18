#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.weight = w;
        this.height = h;
      }
    }

    print() {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.height; i++) {
          console.log('x');
        }
      }
    }

    rotate() {
        let tmp = this.weight;
        this.weight = this.height;
        this.height = tmp;
    }
    double() {
        this.height *= 2;
        this.weight *= 2;
    }
  }
module.exports = Rectangle;
