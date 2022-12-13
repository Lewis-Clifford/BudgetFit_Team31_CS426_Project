import React from 'react'
import {StyledForm, RegisterButton, StyledFormButtom, Img, Title, EnterDetails, ButtonGroup, DontHave, ForgotPass  } from '../login/logincreation'
import {Formik, Form} from 'formik';
import { Input } from '../login/form';
import { MutatingDots } from 'react-loader-spinner'
import {FiUser, FiLock, FiMail} from 'react-icons/fi'

import * as Yup from 'yup';

const Register = () => {
  return (
    <div>
      <StyledForm>
      <Img/> 
        <Title>Register</Title>
        <EnterDetails>Enter your details below to register a new account</EnterDetails>
        <Formik initialValues={{ Email: "", User: "", Pass: "", ConfirmPass: ""}} 
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
        .matches(/^(?=.*[0-9])/, 'Password must contain at least one number'),
        Email: Yup.string("Please enter an email")
        .email("Invalid email address")
        .required("Email required"),
        ConfirmPass: Yup.string("Confirm your password")
        .required("Confirm password required")
        .oneOf([Yup.ref("Pass")], "Passwords must match")
        }) }
        onSubmit = {(values, {setSubmitting}) => {console.log(values)}}
        >

        {({isSubmitting}) => (
        <Form> 
          <Input name="User" type="user" placeholder="Username" icon={<FiUser/>}></Input>
          <Input name="Email" type="email" placeholder="Email address" icon={<FiMail/>}></Input>
          <Input name="Pass" type="password" placeholder="Password" icon={<FiLock/>}></Input>
          <Input name="ConfirmPass" type="password" placeholder="Confirm your password" icon={<FiLock/>}></Input>
          <ForgotPass>Forgot Password?</ForgotPass>
          <ButtonGroup>
            {!isSubmitting && (<StyledFormButtom type="submit">Register</StyledFormButtom>)}

            {isSubmitting && (<MutatingDots color="#73b464" secondaryColor= '#474b4f' radius='12' height="100px" width="100px" />)}
          </ButtonGroup>
          <DontHave>Already registered? Login Below</DontHave>
          <ButtonGroup>
            <RegisterButton to = "/login">Login</RegisterButton>
          </ButtonGroup>
        </Form>
        )}
        </Formik>
      </StyledForm>
      
    </div>
  )
}

export default Register