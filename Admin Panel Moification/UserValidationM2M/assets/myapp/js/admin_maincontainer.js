document.addEventListener('DOMContentLoaded', function() {
    const userField = document.querySelector('#id_user');
    const profileListField = document.querySelector('#id_profilelist');
    
    function updateProfileList() {
        const selectedUser = userField.value;
        if (!selectedUser) {
            profileListField.innerHTML = '';
            return;
        }
        
        fetch(`/admin/get_user_profiles/?user_id=${selectedUser}`)
            .then(response => response.json())
            .then(data => {
                profileListField.innerHTML = '';
                data.forEach(profile => {
                    const option = document.createElement('option');
                    option.value = profile.id;
                    option.textContent = `${profile.user__username} ${profile.age}`;
                    profileListField.appendChild(option);
                });
            });
    }

    userField.addEventListener('change', updateProfileList);
    
    // Initial call to populate profile list if user is pre-selected
    if (userField.value) {
        updateProfileList();
    }
});
