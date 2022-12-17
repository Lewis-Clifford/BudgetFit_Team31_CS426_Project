import './App.css';
import { useState } from "react";
import Axios from "axios";


function App() {
  
    const [name, setName] = useState('');
    const [age, setAge] = useState(0);
    const [gender, setGender] = useState('');
    const [routineType, setRoutineType] = useState('');
    const [dietType, setDietType] = useState('');
    
    const displayInfo = () => {
        console.log(name + age + gender + routineType + dietType);
    };
    
    const [exerciseUserList, setExerciseUserList] = useState([]);
    
    const addExerciseUser = () => {
        Axios.post("http://localhost:3001/create", {
            name: name,
            age: age,
            gender: gender,
            routineType: routineType,
            dietType: dietType
        }).then(() => {
            setExerciseUserList([...exerciseUserList, {
                name: name,
                age: age,
                gender: gender,
                routineType: routineType,
                dietType: dietType
            }]);
        });
    };
    
    const getExerciseUsers = () => {
        Axios.get("http://localhost:3001/exerciseUsers").then((response) => {
            setExerciseUserList(response.data);
        });
    };

    return (
        <div className="App">
            <div className="information">
                <label>Name:</label>
                <input type="text" onChange={(event) => {
                    setName(event.target.value);
                }} />
                <label>Age:</label>
                <input type="number" onChange={(event) => {
                    setAge(event.target.value);
                }} />
                <label>Biological gender:</label>
                <input type="text" onChange={(event) => {
                    setGender(event.target.value);
                }} />
                <label>Routine type:</label>
                <input type="text" onChange={(event) => {
                    setRoutineType(event.target.value);
                }} />
                <label>Diet type:</label>
                <input type="text" onChange={(event) => {
                    setDietType(event.target.value);
                }} />
                <button onClick=(addExerciseUser)>Add Exercise User</button>
            </div>
            <div className="exerciseUsers">
                <button onClick=(getExerciseUsers)>Show Exercise Users</button>
                {exerciseUserList.map((val, key) => {
                    return <div className="exerciseUser">
                        <h3>Name: {val.name}</h3>
                        <h3>Age: {val.age}</h3>
                        <h3>Gender: {val.gender}</h3>
                        <h3>Routine: {val.routineType}</h3>
                        <h3>Diet: {val.dietType}</h3>
                    </div>;
                })}
            </div>
        </div>
    );
}

export default App;
