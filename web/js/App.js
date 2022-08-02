class App extends React.Component
{
	constructor()
	{
		super();
		this.state={
			username: "",
			password: "",
			obj: null,
			progress: 0,
			users: [],
			currentUser: null
		}
	}
	handleBotMsg=()=>{
		alert("Click 'OK' button if you resolve bot detect.");
		eel.settle()();
	}
	complete=()=>{
		alert("Complete!");
	}
	inputChange=(e)=>{
		this.setState({[e.target.name]:e.target.value});
	}
	getUsers= async (e)=>{
		let users=await eel.getUsers()();
		this.setState({users});
	}
	addUser=async (e)=>{
		await eel.addUser(this.state.username,this.state.password)();
		this.setState({
			username: "",
			password: ""
		});
		this.getUsers();
	}
	userChange=(e)=>{
		let dataset=e.target.options[e.target.selectedIndex].dataset;
		this.setState({
			currentUser: {
				username: dataset.username,
				password: dataset.password
			}
		});
	}
	startClick=(e)=>{
		let obj=this.state.obj;
		Object.entries(obj).map(([key,value])=>{
			obj[key].status="";
		});
		this.setState({
			progress: 0,
			obj
		});
		let user=this.state.currentUser;
		eel.start(user.username,user.password);
	}
	setTriviaStatus=(url,status)=>
	{
		let obj=this.state.obj;
		let progress=this.state.progress;
		if(obj[url].status==status)
			return;
		obj[url].status=status;
		this.setState({obj,progress:progress+1});
	}
	async componentDidMount()
	{
		eel.expose(this.setTriviaStatus,"setTriviaStatus");
		eel.expose(this.handleBotMsg,"handleBotMsg");
		eel.expose(this.complete,"complete");
		
		let json=await fetch("./questions.json").then(r=>r.json());
		let obj={};
		let i=1;
		json.forEach(url=>{
			obj[url]={
				name: `${i}. ${url.substring(url.lastIndexOf("/")+1)}`,
				status:"",
				index: i
			};
			i++;
		});
		this.setState({obj});
		this.getUsers();
	}
	render()
	{
		let progressItems;
		if(this.state.obj)
		{
			progressItems=Object.entries(this.state.obj).map(([key,value])=>{
				if(value.index>10) return "";
				return (
					<li key={key} className="list-group-item d-flex justify-content-between align-items-center">
						{value.name}
						<span className="badge bg-primary rounded-pill">{value.status}</span>
					</li>
				);
			})
		}
		return (
			<div className="container">
				<h3 className="my-3">Wizard101 Trivia Autoresponder</h3>
				<div className="input-group mb-3">
					<input type="text" name="username" className="form-control" placeholder="Username" value={this.state.username} onChange={this.inputChange} />
					<input type="password" name="password"  className="form-control" placeholder="Password" value={this.state.password} onChange={this.inputChange} />
					<button className="btn btn-primary" onClick={this.addUser}>Add</button>
				</div>
				<div className="input-group mb-3">
					<label className="input-group-text">Existed Accounts</label>
					<select className="form-select" onChange={this.userChange}>
						<option value="default">Choose...</option>
						{
							this.state.users.map(user=>{
								return (
									<option key={user.username} data-username={user.username} data-password={user.password}>
										{user.username}
									</option>
								);
							})
						}
					</select>
					<button className="btn btn-primary" onClick={this.startClick}>Start</button>
				</div>
				<div className="mb-3">
					<ul className="list-group">
						{progressItems}
					</ul>
				</div>
				<div className="progress mb-3">
					<div className="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style={{width:`${this.state.progress*10}%`}}>{this.state.progress*10}%</div>
				</div>
			</div>
		);
	}
}