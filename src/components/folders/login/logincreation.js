import styled from 'styled-components';
import { Link as LinkRouter } from 'react-router-dom';
import Logo from "../../../components/BF.png"



export const StyledInput = styled.input`
width: 370px;
padding: 10px;
padding-left: 50px;
font-size: 20px;
letter-spacing: 0px;
color: #474b4f;
background-color: #ededed ;
border: none;
border-bottom: solid;
border-bottom-color: #72b264;
display: block;
outline: 0;
margin: 5px auto 15px auto;
transition: ease-in-out 0.5s;

${(props) => props.invalid && `border-bottom-color: red; color: brown`}

&:focus{
  border-bottom-color: #0951d9;
}
`

export const Label = styled.p`
text-align: left;
font-size: 13px;
font-weight: bold;

`

export const StyledForm = styled.div`
background-color: #fff;
text-align: center;
padding: 45px 55px;
width: 500px;
margin-left: auto;
margin-right: auto;
margin-top: 60px;
display: block;
border: solid;
border-color: #72b264;
border-width: 100px;
border-image-slice: 1;
border-image-source: linear-gradient(#72b264 , #474b4f);


`

export const StyledFormButtom = styled.button`
padding: 10px;
width: 430px;
background-color: #72b264;
font-size: 16px;
border: 4px solid #72b264;
color: #fff;
transition: ease-in-out 0.2s;

&:hover{
  background-color: #474b4f;
  border: 4px solid #474b4f;
  color: #fff;
  cursor: pointer;
}

&:active {
  background-color: #72b264;
  border: 4px solid #72b264;
  color: #474b4f
}
`

export const RegisterButton = styled(LinkRouter)`
padding: 10px;
width: 405px;
background-color: #72b264;
font-size: 16px;
border: 4px solid #72b264;
color: #fff;
transition: ease-in-out 0.2s;
text-decoration: none;


&:hover{
  background-color: #474b4f;
  border: 4px solid #474b4f;
  color: #fff;
  cursor: pointer;
}

&:active {
  background-color: #72b264;
  border: 4px solid #72b264;
  color: #474b4f
}
`


export const Img = styled.div`
width: 80px;
height: 80px;
background-image: url(${Logo});
background-size: cover;
background-position: center;
margin: left;
`

export const Title = styled.h2`
font-size: 45px;
text-align: center;
color: #72b264;
margin-top: -25px;

`
export const EnterDetails = styled.p`
font-size: 20px;
text-align: center;
color: #474b4f;
margin: -25px 145px 0px;
`

export const ButtonGroup = styled.div`
display: flex;
justify-content: space-around;
flex-direction: row;
margin-top: 40px;
margin-bottom: 25px;
`

export const DontHave = styled.p`
font-size: 20px;
text-align: center;
color: #474b4f;
margin: -10px 80px -20px;
`

export const ForgotPass = styled.p`
font-size: 15px;
text-align: right;
color: #474b4f;
margin: -10px 40px -20px;
cursor: pointer;
&:active{
  text-decoration: underline;
} 
` 
export const Icon = styled.p`
color: #474b4f;
position: absolute;
font-size 20px;
top: -9.6px;
left: 50px;
${(props) => props.right && `left: 420px; `}
`

export const YupError =  styled.div`
font-size: 13px;
color: red;
margin-top: -5px;
margin-bottom: 10px;
text-align: left;
margin-left: 35px;

`


