'use client'
import React, { useEffect, useState } from 'react'

function page() {
    
  const [Day_1, setDay1] = useState([]);
  const [Day_2, setDay2] = useState([]);
  const [Day_3, setDay3] = useState([]);
  const [Day_4, setDay4] = useState([]);
  const [Day_5, setDay5] = useState([]);
  const [Day_6, setDay6] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8080/test')
    .then((response) => response.json())
    .then((data) => {
      // day = "Loading"
      // once data is retrieved
      // day = data.day
      setDay1(data.Day_1);
      setDay2(data.Day_2);
      setDay3(data.Day_3);
      setDay4(data.Day_4);
      setDay5(data.Day_5);
      setDay6(data.Day_6);
      console.log(data.Day_1)
    });
  }, []);

  return (
<div>
  {Day_1.map((the_day, index) => (
  <div key={index}><b>DAY 1</b> {the_day}<br/><br/><br/></div>
  ))}
    {Day_2.map((the_day, index) => (
  <div key={index}><b>DAY 2</b> {the_day}<br/><br/><br/></div>
  ))}
    {Day_3.map((the_day, index) => (
  <div key={index}><b>DAY 3</b> {the_day}<br/><br/><br/></div>
  ))}
    {Day_4.map((the_day, index) => (
  <div key={index}><b>DAY 4</b> {the_day}<br/><br/><br/></div>
  ))}
    {Day_5.map((the_day, index) => (
  <div key={index}><b>DAY 5</b> {the_day}<br/><br/><br/></div>
  ))}
    {Day_6.map((the_day, index) => (
  <div key={index}><b>DAY 6</b> {the_day}<br/><br/><br/></div>
  ))}
</div>
  )
  }

export default page