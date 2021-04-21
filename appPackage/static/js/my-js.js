'use strict'

function loadData(data, type){
	if(type == "Machine"){
		document.querySelector("#descriptionMachine").value = data['descriptionMachine'];
		if(document.querySelector("#nameMachine"))
			document.querySelector("#nameMachine").value = data['nameMachine'];
	}
	else if(type == "Component"){
		if(document.querySelector('#form-update-component')){
			document.querySelector('#nameComponent').value = data["nameComponent"];
			document.querySelector('#typeComponent').value = data["typeComponent"];
			document.querySelector('#priority').value = data["priority"];
			document.querySelector('#notes').value = data['notes'];
			document.querySelector('#minimumStock').value = data['minimumStock'];
		}
		else{		
			document.querySelector('#nameComponent').value = data["nameComponent"];
			switch(data["typeComponent"]) {
				case 1: document.querySelector('#typeComponent').value = "Electrico"; break;
				case 2: document.querySelector('#typeComponent').value = "Mecanico"; break;
				case 3: document.querySelector('#typeComponent').value = "Neumatico"; break;
				case 4: document.querySelector('#typeComponent').value = "Hidraulico"; break;
				case 5: document.querySelector('#typeComponent').value = "Quimico"; break;
				default: document.querySelector('#typeComponent').value = "--"; break;
			}
			switch(data["priority"]) {
				case 1: document.querySelector('#priority').value = "A"; break;
				case 2: document.querySelector('#priority').value = "B"; break;
				case 3: document.querySelector('#priority').value = "C"; break;
				default: document.querySelector('#priority').value = "--"; break;
			}
			document.querySelector('#notes').value = data['notes'];
			document.querySelector('#currentStock').value = data['currentStock'];
			document.querySelector('#minimumStock').value = data['minimumStock'];
		}
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

if(document.querySelector('#ver-maquina') || document.querySelector('#form-update-machine')){
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

if(document.querySelector('#form-update-component')){
	let listComponents = document.querySelector('#codeComponent');
	listComponents.addEventListener('change', function(){
		getList("/verComponente", "Component", listComponents.value);
	});
	listComponents.value = "";
	document.querySelector('#typeComponent').value = "";
	document.querySelector('#priority').value = "";
}