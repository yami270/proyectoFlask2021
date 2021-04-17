'use strict'

function loadData(data, type){
	if(type == "Machine"){
		document.querySelector("#descriptionMachine").value = data['descriptionMachine'];
	}
	else if(type == "Component"){
		document.querySelector('#nameComponent').value = data["nameComponent"];
		if(data["typeComponent"] == 1)
			document.querySelector('#typeComponent').value = "Electrico";
		else if(data["typeComponent"] == 2)
			document.querySelector('#typeComponent').value = "Mecanico";
		else if(data["typeComponent"] == 3)
			document.querySelector('#typeComponent').value = "Neumatico";
		else if(data["typeComponent"] == 4)
			document.querySelector('#typeComponent').value = "Hidraulico";
		else
			document.querySelector('#typeComponent').value = "Quimico";

		if(data["priority"] == 1)
			document.querySelector('#priority').value = "A";
		else if(data["priority"] == 2)
			document.querySelector('#priority').value = "B";
		else if(data["priority"] == 3)
			document.querySelector('#priority').value = "C";
		else
			document.querySelector('#priority').value = "-";

		document.querySelector('#notes').value = data['notes'];
		document.querySelector('#currentStock').value = data['currentStock'];
		document.querySelector('#minimumStock').value = data['minimumStock'];
	}
}

function getList(url, type, value){
	let urlRequest = window.location.origin + url; 
	let tokenCSRF = document.querySelector('#csrf_token').value;
	let listParameters = {};
	listParameters["code"+type] = value;
	const request = new XMLHttpRequest();
	request.open("post", urlRequest, true);
	request.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
	request.setRequestHeader('Content-type', 'application/json;');
	request.setRequestHeader('X-CSRF-TOKEN', tokenCSRF);
	request.send(JSON.stringify(listParameters));
	request.onreadystatechange =  function(){
		if(this.readyState == 4 && this.status == 200){
			const data = JSON.parse(this.responseText); 
			loadData(data, type);
		}
	};
}

if(document.querySelector('#ver-maquina')){
	let listMachines = document.querySelector('#codeMachine');
	listMachines.addEventListener('change', function(){
		getList("/verMaquina", "Machine", listMachines.value);
	});
	listMachines.value = "";
}

if(document.querySelector('#ver-componente')){
	let listComponents = document.querySelector('#codeComponent');
	listComponents.addEventListener('change', function(){
		getList("/verComponente", "Component", listComponents.value);
	});
	listComponents.value = "";
}