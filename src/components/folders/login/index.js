import React from 'react'
import {Label, StyledForm, StyledFormButtom, Img, Title, EnterDetails, StyledInput, ButtonGroup, DontHave, ForgotPass  } from './logincreation'
import {Formik, Form} from 'formik';
import { Input } from './form';
import {FiUser, FiLock} from 'react-icons/fi'

const LoginForm = () => {
  return (
    <div>
      <StyledForm>
      <Img/> 
        <Title>Login</Title>
        <EnterDetails>Enter your details below to sign into your account</EnterDetails>
        <Formik initialValues={{ User: "", Pass: "" }}>
        {() => (
        <Form>
          <Input name="User" type="user" placeholder="Username" icon={<FiUser/>}></Input>
          <Input name="Pass" type="password" placeholder="Password" icon={<FiLock/>}></Input>
          <ForgotPass>Forgot Password?</ForgotPass>
          <ButtonGroup>
            <StyledFormButtom>Login</StyledFormButtom>
          </ButtonGroup>
          <DontHave>Don't have an account? Register Below</DontHave>
          <ButtonGroup>
            <StyledFormButtom>Register</StyledFormButtom>
          </ButtonGroup>
        </Form>
        )}
        </Formik>
      </StyledForm>
      
    </div>
  )
}

export default LoginForm