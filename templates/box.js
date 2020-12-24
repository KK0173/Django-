function Pipe() {
  this.spacing = 150;
  this.top = random(height / 6-100, 3 / 4 * height-100);
  this.bottom = height - (this.top + this.spacing);
  this.x = width;
  this.w = 80;
  this.speed = 6;

  var a=this.top-75
    var b=this.w

  this.highlight = false;

  this.hits = function(bird) {
    if (bird.y < height - this.bottom & bird.y > this.top) {
      if (bird.x > this.x && bird.x < this.x + this.w) {
        this.highlight = true;
          var a=parseInt(scorebox.value)
          a+=1
          scorebox.value=a
        return true;
      }
    }
    this.highlight = false;
    return false;
  }

  // var fruit=function (){
  //     var y=a
  //     var x=b
  //     var width=80
  //     this.height=150
  //     this.show=function (){
  //         fill(255);
  //         console.log('出现水果'+y)
  //         ellipse(x, y, 70, 70);
  //     }
  // }
  // var fruit=new fruit()



  this.show = function() {
      // fruit.show()
    // fill(0);
    // if (this.highlight) {
    //   fill(125, 0, 0);
    // }
    // rect(this.x, 0, this.w, this.top);
    // rect(this.x, height-this.bottom, this.w, this.bottom);
    // console.log(this.x)
      var y=this.top+40
      var x=this.x
      fill(255);
      rect(x, y, 80,80);
      // if (this.highlight) {
      //     var y=this.top+40
      //     var x=this.x
      //     fill(0);
      //     rect(x, y, 1,1);
      // }
  }

  this.update = function() {
    this.x -= this.speed;
  }

  this.offscreen = function() {
    if (this.x < -this.w) {
      return true;
    } else {
      return false;
    }
  }


}