function download(prof_naam,course_naam,course_date) {
    const filename="maal.txt";
    var pom = document.createElement('a');
    pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + 
  
    encodeURIComponent(prof_naam)+" "+encodeURIComponent(course_naam)+" "+encodeURIComponent(course_date));
    pom.setAttribute('download', filename);
  
    pom.style.display = 'none';
    document.body.appendChild(pom);
  
    pom.click();
  
    document.body.removeChild(pom);
  }
  
