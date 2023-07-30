<template>
    <div class="background"> 
        <img src="../assets/net_logo.jpg">
        <h1>南风榆阅——农家书屋管理网站</h1>

        <div class="router">
        <nav>
            <router-link to="/">数据统计</router-link> 
            <router-link to="/search">书屋查询</router-link> 
            <router-link to="/about">联系我们</router-link> 
        </nav>
        </div>
    </div>
</template>

<style scoped>
.background {
    background-color: #f0e2b5;
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
    display: flex;
    height: 100%;
    align-items: center;
    justify-content: space-between;
}
  nav a {
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
    color: #2c3e50;
    margin-right: 200px;
    margin-left: 10px;
    flex-shrink: 0;
}
  </style>