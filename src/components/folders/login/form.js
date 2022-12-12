import {useField} from 'formik';
import { StyledInput, Label, Icon, YupError} from './logincreation'
import {FiEyeOff, FiEye} from 'react-icons/fi'
import {useState} from 'react';

export const Input = ({icon, ...props}) => {
    const [field, meta] = useField(props);
    const [enable, allowEnable] = useState(false);

    return (
    <div style={{position: "relative"}}>
    <Label htmlFor={props.name}>
        {props.label}
    </Label>
    {props.type !== "password" &&<StyledInput
        invalid = {meta.touched && meta.error}
        {...field}
        {...props}
    />}

    {props.type === "password" && 
    (<StyledInput 
        invalid = {meta.touched && meta.error}
        {...field} 
        {...props}
        type={enable ? "text" : "password"}
        />
        )}
    <Icon>
        {icon}
    </Icon>
    {
        props.type === "password" && (<Icon onClick= {() => allowEnable(!enable)} right>
            {enable && <FiEye cursor="pointer"/> }
            {!enable && <FiEyeOff cursor="pointer"/> }
            </Icon>
    )}

  {meta.touched && meta.error ? (<YupError>{meta.error}</YupError>): (<YupError style={{visibility:"hidden"}}>.</YupError>)}
    </div>
    );
};