document.getElementById('withPackageButton').addEventListener('click', function() {
  // Handle the 'With Package' button click event
  console.log('With Package button clicked');
});

document.getElementById('withoutPackageButton').addEventListener('click', function() {
  // Handle the 'Without Package' button click event
  console.log('Without Package button clicked');
});

document.getElementById('predictButton').addEventListener('click', function() {
  // Get values from the dropdowns
  const dropdown1 = document.getElementById('dropdown1').value;
  const dropdown2 = document.getElementById('dropdown2').value;
  const dropdown3 = document.getElementById('dropdown3').value;
  const dropdown4 = document.getElementById('dropdown4').value;
  const dropdown5 = document.getElementById('dropdown5').value;
  const dropdown6 = document.getElementById('dropdown6').value;

  // Log the selected values (you can send these values to the backend)
  console.log('Dropdown values:', dropdown1, dropdown2, dropdown3, dropdown4, dropdown5, dropdown6);

  // Simulate a prediction response from the backend
  // Replace this part with your backend integration
  const prediction = `Prediction result based on selected values: ${dropdown1}, ${dropdown2}, ${dropdown3}, ${dropdown4}, ${dropdown5}, ${dropdown6}`;

  // Display the prediction result
  document.getElementById('output').innerText = prediction;
});
