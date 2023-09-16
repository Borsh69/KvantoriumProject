function onEntry(entry) {
    entry.forEach(change => {
      if (change.isIntersecting) {
       change.target.classList.add('element-show');
      }
    });
  }
  
let options = {
    threshold: [0] };
  let observer = new IntersectionObserver(onEntry, options);
  let elements = document.querySelectorAll('.main_block');
  
  for (let elm of elements) {
    observer.observe(elm);
  }
let popup = document.getElementById('popup'),
  popupToggle = document.getElementById('pppBtn'),
  popupClose = document.querySelector('.close');
/*
popupToggle.onclick = function(){
    popup.style.display = "block";
    popup.style.opacity = "1";
  };

  popupClose.onclick = function(){
    popup.style.display = "none";
    popup.style.opacity = "0";
  }
*/
  window.onclick = function(e){
    if(e.target == popup){
      popup.style.display = "none";
      popup.style.opacity = "0";
    }
  }
  function sortList() {
    var list, i, switching, b, shouldSwitch;
    list = document.getElementById("id01");
    switching = true;
    /*Make a loop that will continue until
    no switching has been done:*/
    while (switching) {
      //start by saying: no switching is done:
      switching = false;
      b = list.getElementsByTagName("div");
      //Loop through all list-items:
      for (i = 0; i < (b.length - 1); i++) {
        //start by saying there should be no switching:
        shouldSwitch = false;
        /*check if the next item should
        switch place with the current item:*/
        if (b[i].innerHTML.toLowerCase() > b[i + 1].innerHTML.toLowerCase()) {
          /*if next item is alphabetically
          lower than current item, mark as a switch
          and break the loop:*/
          shouldSwitch = true;
          break;
        }
      }
      if (shouldSwitch) {
        /*If a switch has been marked, make the switch
        and mark the switch as done:*/
        b[i].parentNode.insertBefore(b[i + 1], b[i]);
        switching = true;
      }
    }
  }
  function sortListY() {
    var list, i, switching, b, shouldSwitch;
    list = document.getElementById("id01");
    switching = true;
    /*Make a loop that will continue until
    no switching has been done:*/
    while (switching) {
      //start by saying: no switching is done:
      switching = false;
      b = list.getElementsByTagName("div");
      //Loop through all list-items:
      for (i = 0; i < (b.length - 1); i++) {
        //start by saying there should be no switching:
        shouldSwitch = false;
        /*check if the next item should
        switch place with the current item:*/
        if (b[i].innerHTML.toLowerCase() < b[i + 1].innerHTML.toLowerCase()) {
          /*if next item is alphabetically
          lower than current item, mark as a switch
          and break the loop:*/
          shouldSwitch = true;
          break;
        }
      }
      if (shouldSwitch) {
        /*If a switch has been marked, make the switch
        and mark the switch as done:*/
        b[i].parentNode.insertBefore(b[i + 1], b[i]);
        switching = true;
      }
    }
  }
function Sim(sldrId) {

    let id = document.getElementById(sldrId);
    if(id) {
      this.sldrRoot = id
    }
    else {
      this.sldrRoot = document.querySelector('.sim-slider')
    };
  
    // Carousel objects
    this.sldrList = this.sldrRoot.querySelector('.sim-slider-list');
    this.sldrElements = this.sldrList.querySelectorAll('.sim-slider-element');
    this.sldrElemFirst = this.sldrList.querySelector('.sim-slider-element');
    this.leftArrow = this.sldrRoot.querySelector('div.sim-slider-arrow-left');
    this.rightArrow = this.sldrRoot.querySelector('div.sim-slider-arrow-right');
    this.indicatorDots = this.sldrRoot.querySelector('div.sim-slider-dots');
  
    // Initialization
    this.options = Sim.defaults;
    Sim.initialize(this)
  };
  
  Sim.defaults = {
  
    // Default options for the carousel
    loop: true,     // Бесконечное зацикливание слайдера
    auto: true,     // Автоматическое пролистывание
    interval: 5000, // Интервал между пролистыванием элементов (мс)
    arrows: true,   // Пролистывание стрелками
    dots: true      // Индикаторные точки
  };
  
  Sim.prototype.elemPrev = function(num) {
    num = num || 1;
  
    let prevElement = this.currentElement;
    this.currentElement -= num;
    if(this.currentElement < 0) this.currentElement = this.elemCount-1;
  
    if(!this.options.loop) {
      if(this.currentElement == 0) {
        this.leftArrow.style.display = 'none'
      };
      this.rightArrow.style.display = 'block'
    };
    
    this.sldrElements[this.currentElement].style.opacity = '1';
    this.sldrElements[prevElement].style.opacity = '0';
  
    if(this.options.dots) {
      this.dotOn(prevElement); this.dotOff(this.currentElement)
    }
  };
  
  Sim.prototype.elemNext = function(num) {
    num = num || 1;
    
    let prevElement = this.currentElement;
    this.currentElement += num;
    if(this.currentElement >= this.elemCount) this.currentElement = 0;
  
    if(!this.options.loop) {
      if(this.currentElement == this.elemCount-1) {
        this.rightArrow.style.display = 'none'
      };
      this.leftArrow.style.display = 'block'
    };
  
    this.sldrElements[this.currentElement].style.opacity = '1';
    this.sldrElements[prevElement].style.opacity = '0';
  
    if(this.options.dots) {
      this.dotOn(prevElement); this.dotOff(this.currentElement)
    }
  };
  
  Sim.prototype.dotOn = function(num) {
    this.indicatorDotsAll[num].style.cssText = 'background-color:#556; cursor:pointer;'
  };
  
  Sim.prototype.dotOff = function(num) {
    this.indicatorDotsAll[num].style.cssText = 'background-color:#BBB; cursor:default;'
  };
  
  Sim.initialize = function(that) {
  
    // Constants
    that.elemCount = that.sldrElements.length; // Количество элементов
  
    // Variables
    that.currentElement = 0;
    let bgTime = getTime();
  
    // Functions
    function getTime() {
      return new Date().getTime();
    };
    function setAutoScroll() {
      that.autoScroll = setInterval(function() {
        let fnTime = getTime();
        if(fnTime - bgTime + 10 > that.options.interval) {
          bgTime = fnTime; that.elemNext()
        }
      }, that.options.interval)
    };
  
    // Start initialization
    if(that.elemCount <= 1) {   // Отключить навигацию
      that.options.auto = false; that.options.arrows = false; that.options.dots = false;
      that.leftArrow.style.display = 'none'; that.rightArrow.style.display = 'none'
    };
    if(that.elemCount >= 1) {   // показать первый элемент
      that.sldrElemFirst.style.opacity = '1';
    };
  
    if(!that.options.loop) {
      that.leftArrow.style.display = 'none';  // отключить левую стрелку
      that.options.auto = false; // отключить автопркрутку
    }
    else if(that.options.auto) {   // инициализация автопрокруки
      setAutoScroll();
      // Остановка прокрутки при наведении мыши на элемент
      that.sldrList.addEventListener('mouseenter', function() {clearInterval(that.autoScroll)}, false);
      that.sldrList.addEventListener('mouseleave', setAutoScroll, false)
    };
  
    if(that.options.arrows) {  // инициализация стрелок
      that.leftArrow.addEventListener('click', function() {
        let fnTime = getTime();
        if(fnTime - bgTime > 1000) {
          bgTime = fnTime; that.elemPrev()
        }
      }, false);
      that.rightArrow.addEventListener('click', function() {
        let fnTime = getTime();
        if(fnTime - bgTime > 1000) {
          bgTime = fnTime; that.elemNext()
        }
      }, false)
    }
    else {
      that.leftArrow.style.display = 'none'; that.rightArrow.style.display = 'none'
    };
  
    if(that.options.dots) {  // инициализация индикаторных точек
      let sum = '', diffNum;
      for(let i=0; i<that.elemCount; i++) {
        sum += '<span class="sim-dot"></span>'
      };
      that.indicatorDots.innerHTML = sum;
      that.indicatorDotsAll = that.sldrRoot.querySelectorAll('span.sim-dot');
      // Назначаем точкам обработчик события 'click'
      for(let n=0; n<that.elemCount; n++) {
        that.indicatorDotsAll[n].addEventListener('click', function() {
          diffNum = Math.abs(n - that.currentElement);
          if(n < that.currentElement) {
            bgTime = getTime(); that.elemPrev(diffNum)
          }
          else if(n > that.currentElement) {
            bgTime = getTime(); that.elemNext(diffNum)
          }
          // Если n == that.currentElement ничего не делаем
        }, false)
      };
      that.dotOff(0);  // точка[0] выключена, остальные включены
      for(let i=1; i<that.elemCount; i++) {
        that.dotOn(i)
      }
    }
  };
  new Sim();

