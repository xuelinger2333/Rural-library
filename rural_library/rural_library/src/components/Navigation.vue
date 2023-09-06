<template>
    <div class="background"> 
        <img src="../assets/net_logo.jpg">
        <h1>南风愉阅——农家书屋管理网站</h1>

        <div class="router">
        <nav>
            <router-link to="/"><li>数据统计</li></router-link> 
            <router-link to="/search"><li>书屋查询</li></router-link> 
            <router-link to="/about"><li>联系我们</li></router-link> 
        </nav>
        </div>
    </div>
</template>

<style scoped>
.background {
    background-color: #f2cd89;
    width: 100%;
    height: 60px;
    position: fixed;
    top: 0px;
    left: 0px;
    z-index: 100;
    display: flex ; 
    align-items: center;
}

.router{
    height: 100%;
    display: inline-block;
    flex-basis: 400px;
    flex-shrink: 0;
}
nav {
    list-style-type: none;
    display: flex;
    height: 100%;
    align-items: center;
    justify-content: space-between;
}

nav li:hover{
  color: #edece8;
}
  nav a {
    font-family: "Kyo";
    font-weight: bold;
    color: #2c3e50;
    text-decoration: none;

  }
  nav a.router-link-exact-active {
    color: #9c8e60;
  }
  img {
    height: 100%;
}
h1 {
    font-weight: bold;
    font-family: 'Kyo';
    color: #2c3e50;
    margin-right: 200px;
    margin-left: 10px;
    flex-shrink: 0;
}
  </style>