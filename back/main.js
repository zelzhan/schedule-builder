
import { HttpClient } from '@angular/common/http';

export class AppComponent {
  serverData: JSON;
  employeeData: JSON;
  
  constructor(private httpClient: HttpClient) {
  }


  // sayHi() {
  //   this.httpClient.get('http://127.0.0.1:5002/').subscribe(data => {
  //     this.serverData = data as JSON;
  //     console.log(this.serverData);
  //   })
  // }

  // getAllEmployees() {
  //   this.httpClient.get('http://127.0.0.1:5002/employees').subscribe(data => {
  //     this.employeeData = data as JSON;
  //     console.log(this.employeeData);
  //   })
  // }
}