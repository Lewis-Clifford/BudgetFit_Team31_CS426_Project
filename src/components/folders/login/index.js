import React from 'react'
import {StyledForm, Bar, RegisterButton, StyledFormButtom, Img, Title, EnterDetails, ButtonGroup, DontHave, ForgotPass  } from './logincreation'
import {Formik, Form} from 'formik';
import { Input } from './form';
import { MutatingDots } from 'react-loader-spinner'
import {FiUser, FiLock} from 'react-icons/fi'

import * as Yup from 'yup';

const LoginForm = () => {
  return (
    <div>
      <StyledForm>
      <Img/> 
        <Title>Login</Title>
        <EnterDetails>Enter your details below to sign into your account</EnterDetails>
        <Formik initialValues={{ User: "", Pass: "" }} 
        validationSchema={Yup.object({
        User: Yup.string("Please enter a username") 
        .required("Username required") 
        .matches(/^(?=.*[a-z])/, 'Password must contain at least one letter')
        .min(6, "Username must be atleast 6 characters") 
        .max(16, "Username must be 16 characters or less")
        .matches(/^[a-zA-Z0-9\$]+$/, "Username can only contains letters, digits, and $"),
        Pass: Yup.string("Please enter a password")
        .required("Password required")
        .min(6, "Password must be atleast 6 characters")
        .max(16, "Password must be 16 characters or less")
        .matches(/^[a-zA-Z0-9\$@]+$/, "Password can only contain letters, digits, $, and @ ")
        .matches(/^(?=.*[A-Z])/, 'Password must contain at least one uppercase character')
        .matches(/^(?=.*[0-9])/, 'Password must contain at least one number')

        }) }
        onSubmit = {(values, {setSubmitting}) => {console.log(values)}}
        >

        {({isSubmitting}) => (
        <Form>
          <Input name="User" type="user" placeholder="Username" icon={<FiUser/>}></Input>
          <Input name="Pass" type="password" placeholder="Password" icon={<FiLock/>}></Input>
          <ForgotPass>Forgot Password?</ForgotPass>
          <ButtonGroup>
            {!isSubmitting && (<StyledFormButtom type="submit">Login</StyledFormButtom>)}

            {isSubmitting && (<MutatingDots color="#73b464" secondaryColor= '#474b4f' radius='12' height="100px" width="100px" />)}
          </ButtonGroup>
          <DontHave>Don't have an account? Register Below</DontHave>
          <ButtonGroup>
            <RegisterButton to = "/signup">Register</RegisterButton>
          </ButtonGroup>
        </Form>
        )}
        </Formik>
      </StyledForm>
      
    </div>
  )
}

export default LoginForm