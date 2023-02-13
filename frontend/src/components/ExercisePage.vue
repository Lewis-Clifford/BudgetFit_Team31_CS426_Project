<template>
<div class="styledformE">
<h1 class="ETitle">Want a personally tailored workout? </h1>
<h2 class="ETitle2">For you to be able to receive the most accurate and beneficial workout plan 
for your body composition it is advised to complete these optional questions. *Pressing skip will 
not provide the most optimal workout routine.*</h2>


<FormKit type="form" submit-label="Finish" :submit-attrs="{wrapperClass: 'ButtonGroup', inputClass:'LogButtonE'}">
<div class="inputs">

<FormKit validation="required" inner-class="text" type="number" label="Enter Age" placeholder="Age" :floating-label="false"></FormKit>
</div>
<div class="inputs">
<FormKit validation="required" inner-class="select" type="select" label="Enter Gender" placeholder="Gender" :options="['Male', 'Female', 'Non-Binary', 'Prefer not to say']" ></FormKit>
</div>
<div class="inputs">
<FormKit validation="required" inner-class="textW" label-class="labelW" type="number" label="Enter Weight" placeholder="Weight" :floating-label="false"></FormKit>
</div>
<div class="inputs">
  <FormKit validation="required" inner-class="textWH" label-class="labelW" type="number" label="Enter Height  " placeholder="Height (Inches)" :floating-label="false"></FormKit>
</div>
<FormKit validation="required" lable-class="labelR" type="range" v-model="value" label="What is your workout experience (1-5)?" min="1" max="5"></FormKit>
<p>{{ value }}</p>
</FormKit>


<router-link to="/exercise/exercise1">
        <button class="Skipbutton">Skip</button>
      </router-link>
    

</div>


</template>


<script>


export default{
    name: 'ExercisePage',
    data(){
      return{
        value: "1", 
        FormData: {

        }
      }
    }
  
}

</script>
 


<style>
.LogButtonE{
padding: 10px !important;
width: 395px !important;
border-radius: var(--fk-border-radius) !important;
background-color: #72b264 !important;
font-size: 16px !important;
border: 4px solid #72b264 !important;
color: #fff !important;
transition: ease-in-out 0.2s !important;
}

.LogButtonE:hover{
  background-color: #474b4f !important;
  border: 4px solid #474b4f !important;
  color: #fff !important;
  cursor: pointer !important;
}

.LogButtonE:active {
  background-color: #72b264 !important;
  border: 4px solid #72b264 !important;
  color: #474b4f !important;
}

.Skipbutton{
padding: 10px;
width: 150px;
background-color: #4d4f47;
font-size: 16px;
border: 4px solid #474b4f;
color: #fff;
transition: ease-in-out 0.2s;
margin-right: 15px;
}

.Skipbutton:hover{
background-color: #72b264;
border: 4px solid #72b264;
color: #fff;
cursor: pointer;
}

.Skipbutton:active {
background-color: #474b4f;
border: 4px solid #474b4f;
color: #474b4f
}

[data-type=number] .formkit-inner{
width: 40px;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 34px;
margin-top: 30px;
height: 50px
}

[data-type] .formkit-label{
 padding-bottom: -30px !important;
 position: relative;
 top: 28px;
 font-weight: normal;
 
}

.labelW{ padding-bottom: -50px !important;
 position: relative;
 top: 28px;
 margin-top: -30px;
 }

.labelR{
  
 display: none !important;
}



.inputs{
  display: inline-block;
  margin-right: 80px;
  margin-bottom: -40px;
}

.text{
 margin-left: -33px;
 margin-bottom: 55px;
 width: 80px !important;
}

.textW{
 margin-left: -33px;
 margin-bottom: 55px;
 width: 100px !important;
}

.textWH{
 margin-left: -33px;
 margin-bottom: 55px;
 width: 180px !important;
}

.select{
  margin-left: -33px;
 margin-bottom: 45px;
 width: 160px !important;
}


.styledformE{
background-color: #fff;
text-align: left;
padding: 45px 55px;
width: auto;
height: auto;
margin-left: auto;
margin-right: auto;
margin-top: 60px;
display: block;
border: solid;
border-color: #72b264;
border-width: 100px;
border-image-slice: 1;
border-image-source: linear-gradient(#72b264 , #474b4f);
}

.ETitle{

    font-size: 45px;
    color:#474b4f;
    text-align: left;
    margin-top: -30px;
    margin-left: -10px;

}

.ETitle2{

font-size: 18px;
color:#97a0ab;
text-align: left;
margin-bottom: -10px;

border-bottom:4px solid black;
padding-bottom: 15px;


}

[data-type="select"] .formkit-inner{
width: 430px;
color: #474b4f;
background-color: white ;
outline: 0;
transition: ease-in-out 0.5s;
left: 34px;
margin-top: 30px;
}

[data-type="select"] .formkit-input{
  line-height: 25px;

}

.LogButtonE{
padding: 10px;
width: 430px;
background-color: #4d4f47;
font-size: 16px;
border: 4px solid #474b4f;
color: #fff;
transition: ease-in-out 0.2s;
}

.LogButtonE:hover{
  background-color: #72b264;
  border: 4px solid #72b264;
  color: #fff;
  cursor: pointer;
}

.LogButtonE:active {
  background-color: #474b4f;
  border: 4px solid #474b4f;
  color: #474b4f
}


</style>