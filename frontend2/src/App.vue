<template>
  <div class="app">
    <router-view/>
  </div>

</template>


<style>

.app{
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: "Courier New Lucida Console Monaco", "Monospace";
  background: rgb(31,31,37);
  background: -moz-linear-gradient(0deg, rgba(31,31,37,1) 33%, rgba(60,73,84,1) 100%);
  background: -webkit-linear-gradient(0deg, rgba(31,31,37,1) 33%, rgba(60,73,84,1) 100%);
  background: linear-gradient(0deg, rgba(31,31,37,1) 33%, rgba(60,73,84,1) 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr="#1f1f25",endColorstr="#3c4954",GradientType=1);  
}

#app{
  height: 100%;
}
</style>