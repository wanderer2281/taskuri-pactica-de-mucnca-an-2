package main
import "fmt"
import "os"
import "bufio"
import "strconv"




func main() {

var path string = os.Args[1]
fmt.Println(path)

var str string = ""
var file_name string =""
var cuv_4 string
var ok int = 0
var number int
var i int


pathinfo , err := os.Stat(path)
if err != nil {
fmt.Println("This path does not exist")
os.Exit(0)
}
if pathinfo.IsDir() {
fmt.Println("The path is a directory")

} else {

fmt.Println("The path is a file")
}



if pathinfo.IsDir(){
    
    dir , err := os.Open(path)
    if err != nil {

    panic(err)

    }

    files, err := dir.Readdir(0)
    if err != nil {
        fmt.Println(err)
        return}

    
    for _, v := range files {
            file_name = v.Name()
            fmt.Println(file_name)
            fmt.Println(file_name[(len(file_name)-2):((len(file_name)))])
            if file_name[(len(file_name)-2):((len(file_name)))] == "in"{
                fmt.Println("File de tip in")
            
            
                file,err := os.Create(path + file_name[0:(len(file_name)-2)] + "in.x")
                if(err !=nil){
                    panic(err)}

            
            
                file_write , ferr :=  os.Open(path + file_name)
                    if ferr!= nil {
            
                        panic(ferr)
                            }
                scanner := bufio.NewScanner(file_write)


            
                for scanner.Scan() { 
                    line := scanner.Text()
                    str = line
                    fmt.Println(str)
                    fmt.Println()
                    i = 0
                    ok =0
                        for i<len(str){
                    
                            if ok==0{
                                _ , err := file.WriteString(string(str[i]))
                                if (err!=nil){
                                panic(err)}
                                }
                            
                            if  str[i] == 32{
                                     ok = 1
                                     i++
                                     
                                     
                                     
                                     
                                     }
                            
                            if ok!=1{
                                fmt.Println(string(str[i]))
                                i++

                                
                                } else if i+3<len(str){
                                        
                                        cuv_4 = str[i:i+4]
                                        number4 , _ := strconv.Atoi(cuv_4)
                                        number = number4
                                        
                                        i = i+4
                            
                                
                                
                                    } else {
                                        cuv_4 = str[i:len(str)]
                                        number4 , _ := strconv.Atoi(cuv_4)
                                        number = number4
                                       
                                        i = len(str)
                                    
                                    
                                    
                                    
                                    }
                            
                            if ok==1 {
                                fmt.Println(number)
                                var number16 int = binarytohex(number)
                                fmt.Println(number16)
                                var numberstr string = hextostring(number16)
                                fmt.Println(numberstr)
                                _ , err := file.WriteString(numberstr)
                                if (err!=nil){
                                panic(err)
                        
                        }        
                        }
                            if i==len(str){
                            
                                 _ , err := file.WriteString("\n")
                                 if (err!=nil){
                                 panic(err)}
                            
                            
                            
                            }
        
        
        
        
        
        }
       


        
        }
        
        
            
        os.Remove(path + file_name)    }
            if file_name[(len(file_name)-2):((len(file_name)))] == ".x"{
                
                file,err := os.Create(path + file_name[0:(len(file_name)-4)] + "in")
                if(err !=nil){
                    panic(err)}

            
            
                file_write , ferr :=  os.Open(path + file_name)
                    if ferr!= nil {
            
                        panic(ferr)
                            }
                scanner := bufio.NewScanner(file_write)

                
                for scanner.Scan() { 
                    line := scanner.Text()
                    str = line
                    fmt.Println(str)
                    fmt.Println()
                    i = 0
                    ok =0
                    for i<len(str){
                
                        if ok==0{
                            _ , err := file.WriteString(string(str[i]))
                            if (err!=nil){
                            panic(err)}
                            }
                        
                        if  str[i] == 32{
                                 ok = 1
                                 i++
                                 
                                 
                                 
                                 
                                 }
                        
                        if ok!=1{
                            fmt.Println(string(str[i]))
                            i++

                            
                            } 
                        
                        if ok==1 {
                            fmt.Println(number)
                            var number16 string = string(str[i])
                            fmt.Println(number16)
                            var numberstr string = hextostringbin(number16)
                            fmt.Println(numberstr)
                            _ , err := file.WriteString(numberstr)
                            if (err!=nil){
                            panic(err)
                            }   
                            i++     
                    }
                        if i==len(str){
                        
                             _ , err := file.WriteString("\n")
                             if (err!=nil){
                             panic(err)}
                        
                        
                        
                        }
        
        
        
        
        
        }
       


        
        }
            
            
            
            
            
            
            
            
            
        os.Remove(path + file_name)  }
    }

fmt.Println(file_name)












}else{
    if path[(len(path)-2):(len(path))] == "in"{
        
        file,err := os.Create(path[0:(len(path)-2)] + "in.x")
        if(err !=nil){
        panic(err)}
        
        file_write , ferr :=  os.Open(path + file_name)
        if ferr!= nil {
            
                        panic(ferr)
                            }
        scanner := bufio.NewScanner(file_write)
        
        
        
        for scanner.Scan() { 
            line := scanner.Text()
            str = line
            fmt.Println(str)
            fmt.Println()
            i = 0
            ok =0
        for i<len(str){
            
                    if ok==0{
                        _ , err := file.WriteString(string(str[i]))
                        if (err!=nil){
                        panic(err)}
                        }
                    
                    if  str[i] == 32{
                             ok = 1
                             i++
                             
                             
                             
                             
                             }
                    
                    if ok!=1{
                        fmt.Println(string(str[i]))
                        i++

                        
                        } else if i+3<len(str){
                                
                                cuv_4 = str[i:i+4]
                                number4 , _ := strconv.Atoi(cuv_4)
                                number = number4
                                
                                i = i+4
                    
                        
                        
                            } else {
                                cuv_4 = str[i:len(str)]
                                number4 , _ := strconv.Atoi(cuv_4)
                                number = number4
                               
                                i = len(str)
                            
                            
                            
                            
                            }
                    
                    if ok==1 {
                        fmt.Println(number)
                        var number16 int = binarytohex(number)
                        fmt.Println(number16)
                        var numberstr string = hextostring(number16)
                        fmt.Println(numberstr)
                        _ , err := file.WriteString(numberstr)
                        if (err!=nil){
                        panic(err)
                
                }        
                }
                    if i==len(str){
                    
                         _ , err := file.WriteString("\n")
                         if (err!=nil){
                         panic(err)}
                    
                    
                    
                    }
            
            
            
            
            
            }
           


            
            }
            
  
    
    
    
    
    
    
    os.Remove(path)  }
  if path[(len(path)-2):(len(path))] == ".x"{  
  
            file,err := os.Create(path[0:(len(path)-4)] + "in")
            if(err !=nil){
                panic(err)}

        
        
            file_write , ferr :=  os.Open(path + file_name)
                if ferr!= nil {
        
                    panic(ferr)
                        }
            scanner := bufio.NewScanner(file_write)

            
            for scanner.Scan() { 
                line := scanner.Text()
                str = line
                fmt.Println(str)
                fmt.Println()
                i = 0
                ok =0
                for i<len(str){
            
                    if ok==0{
                        _ , err := file.WriteString(string(str[i]))
                        if (err!=nil){
                        panic(err)}
                        }
                    
                    if  str[i] == 32{
                             ok = 1
                             i++
                             
                             
                             
                             
                             }
                    
                    if ok!=1{
                        fmt.Println(string(str[i]))
                        i++

                        
                        } 
                    
                    if ok==1 {
                        fmt.Println(number)
                        var number16 string = string(str[i])
                        fmt.Println(number16)
                        var numberstr string = hextostringbin(number16)
                        fmt.Println(numberstr)
                        _ , err := file.WriteString(numberstr)
                        if (err!=nil){
                        panic(err)
                        }   
                        i++     
                }
                    if i==len(str){
                    
                         _ , err := file.WriteString("\n")
                         if (err!=nil){
                         panic(err)}
                    
                    
                    
                    }
    
    
    
    
    
    }
   


    
    }
        

  
  
  
  
  
  
  os.Remove(path)  }


}










}





func binarytohex(number int) int{
    var b int = 1
    var number6 = 0
    for number !=0{
        number6 = number6 + (number%10)*b
        b = b*2
        number = number/10
    }
    return number6
}

func hextostring(number int) string{
    var numberstr string
    if number<10{
        numberstr = strconv.Itoa(number)
    
    }
    if number == 10{
        numberstr="A"}
    if number == 11{
        numberstr="B"}
    if number == 12{
        numberstr="C"}
    if number == 13{
        numberstr="D"}
    if number == 14{
        numberstr="E"}
    if number == 15{
        numberstr="F"}
    
    return numberstr



}

func hextostringbin(number16 string) string{
    var numberstr string
    if number16 == "1"{
        numberstr ="0001"
    
    }
    if number16 == "2"{
        numberstr="0010"}
    if number16 == "3"{
        numberstr="0011"}
    if number16 == "4"{
        numberstr="0100"}
    if number16 == "5"{
        numberstr="0101"}
    if number16 == "6"{
        numberstr="0110"}
    if number16 == "7"{
        numberstr="0111"}
    if number16 == "8"{
        numberstr="1000"}
    if number16 == "9"{
        numberstr="1001"}
    if number16 == "A"{
        numberstr="1010"}
    if number16 == "B"{
        numberstr="1011"}
    if number16 == "C"{
        numberstr="1100"}
    if number16 == "D"{
        numberstr="1101"}
    return numberstr



}



