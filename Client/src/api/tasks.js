import axios from 'axios'

const URL = 'http://localhost:8000'
const endpoint = `${URL}/api/tasks/`
export const fetchTask = async (id) => 
    await axios.get(`${endpoint}${id}`)

export const createTask= async (newTask)=>
    await axios.post(endpoint,newTask)

export const updateTask= async (id,task)=>
    await axios.put(`${endpoint}${id}`,task)

export const deleteTask= async (id)=>
    await axios.delete(`${endpoint}${id}`)

export const fetchTasks = async () => 
    await axios.get(`${endpoint}`)

