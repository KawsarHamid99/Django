console.log("Hello world")
const postBox=document.getElementById('posts-box')
const spinnerBox=document.getElementById('spinner-box')
const loadBtn=document.getElementById('load-btn')
const loadBox=document.getElementById('loading-box')
let visible = 3

const handleGetData = () =>{
    $.ajax({
        type:'GET',
        url: `/posts-json/${visible}/`,
        success:function(response){
            // console.log(response.max)
            max_size=response.max
            const data = response.data
            spinnerBox.classList.remove('not-visible')
            setTimeout(()=>{
                spinnerBox.classList.add('not-visible')
                data.map(post=>{
                    console.log(post.id)
                    postBox.innerHTML += `
                    <tr>
                    <th class="border border-dark" scope="row">${post.id}</th>
                    <td class="border border-dark">${post.name}</td>
                    <td class="border border-dark">${post.email}</td>
                    <td class="border border-dark">${post.faculty}</td>
                    </tr>
                    `
                })

            },500)
            
            if(max_size){
                console.log('done')
                loadBox.innerHTML="<h4>No more posts to load</h4>"
            }
        },
        error:function(error){
            console.log(error)
        }
    })

}
handleGetData()

loadBtn.addEventListener('click', ()=>{
   visible += 3
   handleGetData()
})