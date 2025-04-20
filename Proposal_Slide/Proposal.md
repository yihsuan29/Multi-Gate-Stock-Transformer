---
marp: true
paginate: true
theme: gaia
style: |
  section {
    background-color:rgb(255, 255, 255);
  }
  ul, ol {
    margin: 0; 
    }
  sub, sup {
    font-size: 0.5em;
  }
  img[alt~="center"] {
    display: block;
    margin: 0 auto;
  }
  table {
    font-size: 25px;
  }
  .container{
    display: flex;
    }
    .col{
        flex: 1;
    }
---
<!-- _paginate: tfalse -->

## <br><br>DLP Final Project Prposal:<br>Market Guided Stock Transformer<br>
Group
10705009 陳重光、313551047 陳以瑄、313554043 戴明貴 


---
### Outline

* Intoduction - Market Guided
* MASTER - AAAI'24
* Motivation & Innovation
* Problem Definition

---
### Introduction - Market Guided
Stock prediction features can be divided into two types:
1. Individual Stock Features: 
    * Open price, close price, etc.
    * Trading volume
2. Shared market features:
    * Market index
    * Macroeconomic indicators, e.g. interest rate

---
<style>
img[alt~="top-right"] {
  position: absolute;
  top: 280px;
  right: 80px;
}
</style>

### Introduction - Market Guided
The market feature impacts the effectiveness of other features.

**Example: Short Selling**
When investors believe a stock is overvalued.
1. Borrow stock, sell at high price.
2. Buy back at lower price when it falls.
3. Return to owner.
![top-right height:300px](Images/ShortSelling.png)

---
### Introduction - Market Guided
The market feature impacts the effectiveness of other features.

**Example: Short Selling**
Effectiveness in different market status:
* Bull Market: Short selling loses money, less concern.
* Bear Market: Short selling signals pessimism, more significant.

**→ Using market status to select relevant features.**

---
### MASTER:Market-Guided Stock Transformer for Stock Price Forecasting <sup>[1]</sup>
![height:350px center](./Images/MasterOverview.png)

<!-- _footer: '[1] <a href="https://ojs.aaai.org/index.php/AAAI/article/view/27767">MASTER:Market-Guided Stock Transformer for Stock Price Forecasting -AAAI 24</a>' -->
---
### Motivation & Innovation

---
### Problem Definition

---
### Data Description

---
### Example of footer
MASTER:Market-Guided Stock Transformer for Stock Price Forecasting <sup>[1]</sup>

<!-- _footer: '[1] <a href="https://ojs.aaai.org/index.php/AAAI/article/view/27767">MASTER:Market-Guided Stock Transformer for Stock Price Forecasting</a>' -->

---
### Example of table
|OFTIC|ACTDATS|ESTIMID|ALYSNAM|HORIZON|VALUE|ESTCUR|
|--|--|--|--|--|--|--|
|GOOGL|2015-10-23|GOLDMAN|BELLINI, CFA H|12|42.50|USD|
|2330|2014-10-21|CSCFH|CHEN L| 3|140.000|TWD|

---
### Example of insert images
![height:400px center](./Images/1.png)
