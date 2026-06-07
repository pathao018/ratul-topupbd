from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """

<html>

<head>

<title>Ratul TopupBD</title>

<style>

body{
    margin:0;
    font-family:Arial;
    background:#f4f4f4;
}

.navbar{
    background:white;
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:20px;
    box-shadow:0 0 10px gray;
}

.logo{
    font-size:35px;
    font-weight:bold;
    color:#6a00ff;
}

.menu a{
    text-decoration:none;
    margin:15px;
    color:black;
    font-size:18px;
}

.login{
    background:#6a00ff;
    color:white;
    padding:10px 20px;
    border-radius:10px;
}

.banner{
    background:linear-gradient(to right,#6a00ff,#8c52ff);
    color:white;
    text-align:center;
    padding:60px;
    font-size:40px;
    font-weight:bold;
}

.container{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:30px;
    padding:40px;
}

.card{
    width:260px;
    background:white;
    border-radius:15px;
    overflow:hidden;
    box-shadow:0 0 15px rgba(0,0,0,0.2);
}

.card img{
    width:100%;
    height:180px;
}

.card h2{
    text-align:center;
}

.card p{
    text-align:center;
    color:#6a00ff;
    font-size:20px;
    font-weight:bold;
}

.buy{
    display:block;
    background:#6a00ff;
    color:white;
    text-align:center;
    padding:15px;
    text-decoration:none;
}

.section{
    background:white;
    margin:30px;
    padding:30px;
    border-radius:15px;
    box-shadow:0 0 10px gray;
}

input,select{
    width:100%;
    padding:15px;
    margin-top:15px;
    border-radius:10px;
    border:1px solid gray;
}

button{
    width:100%;
    padding:15px;
    margin-top:20px;
    background:#6a00ff;
    color:white;
    border:none;
    border-radius:10px;
    font-size:20px;
}

.payment{
    display:flex;
    gap:20px;
    margin-top:20px;
}

.paybox{
    flex:1;
    background:#f2f2f2;
    padding:20px;
    border-radius:10px;
    text-align:center;
}

footer{
    background:#111;
    color:white;
    text-align:center;
    padding:20px;
}

</style>

</head>

<body>

<div class="navbar">

<div class="logo">
RATUL TOPUPBD
</div>

<div class="menu">
<a href="#">Home</a>
<a href="#">Topup</a>
<a href="#">Contact</a>
<a class="login" href="#">Login</a>
</div>

</div>

<div class="banner">
🔥 FREE FIRE TOPUP 🔥
</div>

<div class="container">

<div class="card">
<img src="https://wallpapercave.com/wp/wp5128415.jpg">
<h2>Weekly Membership</h2>
<p>160 TK</p>
<a class="buy" href="#">Buy Now</a>
</div>

<div class="card">
<img src="https://wallpapercave.com/wp/wp5128415.jpg">
<h2>Monthly Membership</h2>
<p>800 TK</p>
<a class="buy" href="#">Buy Now</a>
</div>

<div class="card">
<img src="https://wallpapercave.com/wp/wp5128415.jpg">
<h2>520 Diamond</h2>
<p>400 TK</p>
<a class="buy" href="#">Buy Now</a>
</div>

<div class="card">
<img src="https://wallpapercave.com/wp/wp5128415.jpg">
<h2>1060 Diamond</h2>
<p>800 TK</p>
<a class="buy" href="#">Buy Now</a>
</div>

</div>

<div class="section">

<h1>Recharge Form</h1>

<select>
<option>Weekly Membership</option>
<option>Monthly Membership</option>
<option>520 Diamond</option>
<option>1060 Diamond</option>
</select>

<input type="text" placeholder="Enter Free Fire UID">

<div class="payment">

<div class="paybox">

<img src="https://freelogopng.com/images/all_img/1656234782bkash-logo-png.png" width="80">

<h2>Bkash</h2>

<p>01306024754</p>

<input type="text" placeholder="Enter Transaction ID">

</div>

<div class="paybox">

<img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png" width="100">

<h2>Nagad</h2>

<p>01306024754</p>

<input type="text" placeholder="Enter Transaction ID">

</div>

</div>

<button>BUY NOW</button>

</div>

<footer>
© 2026 Ratul TopupBD
</footer>

</body>

</html>

"""

app.run(debug=True)