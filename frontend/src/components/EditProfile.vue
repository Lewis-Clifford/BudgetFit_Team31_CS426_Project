<template>
  <div class="overlay"  v-if="showConfirmationBox"></div>
 <section class="py-5 my-5">
		<div class="container">
			<h1 class="mb-5" style="color: #72b264">Edit Profile</h1>
			<div class="bg-white shadow rounded-lg d-block d-sm-flex">
				<div class="profile-tab-nav border-right">
					<div class="p-4">
            <div class="profile-picture-container profile-picture-wrapper">
              <div class="img-circle text-center mb-3" @click="openFileDialog">
                <img :src="profileImage || defaultprofileImage" class="shadow">
                <div class="change-profile-pic-overlay">
                  Change Profile Picture
                </div>
              </div>
              <input ref="fileInput" type="file" style="display: none;" @change="handleFileInputChange">
            </div>
						<h4 class="text-center">{{username}}</h4>
					</div>
					<div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
						<button class="nav-link active" id="account-tab" data-bs-toggle="pill" data-bs-target="#account" type="button" role="tab" aria-controls="account" aria-selected="true">
						<i class="fa fa-home text-center me-1"></i> 
						Account
					</button>

                    <button class="nav-link " id="password-tab" data-bs-toggle="pill" data-bs-target="#password" type="button" role="tab" aria-controls="password" aria-selected="false">
						<i class="fa fa-key text-center me-1"></i> 
						Password
					</button>
                    <button class="nav-link" id="notification-tab" data-bs-toggle="pill" data-bs-target="#notification" type="button" role="tab" aria-controls="notification" aria-selected="false">
						<i class="fa fa-bell text-center me-1"></i> 
						Notification
					</button>
					</div>
				</div>
				<div class="tab-content p-4 p-md-5" id="v-pills-tabContent">
					<div class="tab-pane fade show active" id="account" role="tabpanel" aria-labelledby="account-tab">
						<h3 class="mb-4">Account Settings</h3>
						<div class="row">
							<div class="col-md-6">
								<div class="form-group">
								  	<label>First Name</label>
								  	<input type="text" class="form-control" v-model="name">
								</div>
							</div>
							<div class="col-md-6">
								<div class="form-group">
								  	<label>Last Name</label>
								  	<input type="text" class="form-control" v-model="lastName">
								</div>
							</div>
							<div class="col-md-6">
								<div class="form-group">
								  	<label>Email</label>
								  	<input type="text" class="form-control" v-model="email">
								</div>
							</div>
							<div class="col-md-6">
								<div class="form-group">
								  	<label>Phone number</label>
								  	<input type="tel" class="form-control" v-model="phoneNumber">
								</div>
							</div>
						</div>
						<div>
              <button class="btn btn-custom" @click="showConfirmationBox = true">Update</button>
            </div>

            <div class="confirmation-box" v-if="showConfirmationBox">
              <div class="confirmation-message">
                <p>Are you sure you want to update your profile?</p>
              </div>
              <div class="confirmation-buttons">
                <button class="btn btn-confirm" @click="sendFormsTogether">Confirm</button>
                <button class="btn btn-cancel" @click="showConfirmationBox = false">Cancel</button>
              </div>
            </div>
          </div>
          <div class="updatedMessage" v-if="showMessage">Profile Updated!</div>
					<div class="tab-pane fade" id="password" role="tabpanel" aria-labelledby="password-tab">
						<h3 class="mb-4">Password Settings</h3>
						<div class="row">
							<div class="col-md-6">
								<div class="form-group">
								  	<label>Old password</label>
								  	<input type="password" class="form-control">
								</div>
							</div>
						</div>
						<div class="row">
							<div class="col-md-6">
								<div class="form-group">
								  	<label>New password</label>
								  	<input type="password" class="form-control"  v-model="password">
								</div>
							</div>
							<div class="col-md-6">
								<div class="form-group">
								  	<label>Confirm new password</label>
								  	<input type="password" class="form-control"  v-model="password">
								</div>
							</div>
						</div>
						<div>
              <button class="btn btn-custom" @click="showConfirmationBox = true">Update</button>
            </div>
            <div class="confirmation-box" v-if="showConfirmationBox">
              <div class="confirmation-message">
                <p>Are you sure you want to update your profile?</p>
              </div>
              <div class="confirmation-buttons">
                <button class="btn btn-confirm" @click="updatePassword">Confirm</button>
                <button class="btn btn-cancel" @click="showConfirmationBox = false">Cancel</button>
              </div>
            </div>
					</div>
          <div class="updatedMessage" v-if="showMessage2">Password Updated!</div>
					<div class="tab-pane fade" id="notification" role="tabpanel" aria-labelledby="notification-tab">
						<h3 class="mb-4">Notification Settings</h3>
						<div class="form-group">
							<div class="form-check">
								<input class="form-check-input" type="checkbox" value="" id="text-notifications" v-model="textNotificationsEnabled" :checked="enableTextNotifications">
								<label class="form-check-label" for="text-notifications">
									Enable Text Notifications (Unfortunately you can't turn them off!)
								</label>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
  </template>
  
  <script>
  import profileImage from '../assets/icon.jpg';
  import store from '../store';
  import sha256 from 'crypto-js/sha256';
  import axios from 'axios';
import { fa } from '@formkit/i18n';
  export default{
    name: 'Edit',
    data() {
    return {
      profileImage: null,
      showConfirmationBox: false,
      email: '',
      name: '',
      lastName: '',
      phoneNumber: '',
      showMessage: false,
      showMessage2: false,
      defaultprofileImage: profileImage,
      password: ''
    };
  },
  methods: {
    openFileDialog() {
      this.$refs.fileInput.click();
    },
    handleFileInputChange(event) {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = () => {
    this.profileImage = reader.result;
  };

  reader.readAsDataURL(file);
},
async getUserProfile(userID) {
  axios.get(`http://localhost:5000/profile?userID=${userID}`)
    .then(response => {
      const data = response.data[0];
      this.email = data.email;
      this.name = data.name;
      this.lastName = data.lastName;
      this.phoneNumber = data.phoneNumber;
      this.profileImage = data.profileImage;

      store.dispatch('updateProfileImage', data.profileImage);
      localStorage.setItem('phone', this.phoneNumber)
      localStorage.setItem('name', this.name)
      
    })
    .catch(error => {
      console.log(error);
    });
},

async updatePassword(){
  const hashedPassword = sha256(this.password).toString();
  try {
      const response = await axios.post('http://localhost:5000/updatePassword', {
        userID: localStorage.getItem('userID'),
        password: hashedPassword
      });
      this.showConfirmationBox = false;
      this.showMessage2 = true;
      setTimeout(() => {
    window.location.reload();
  }, 1000);
      setTimeout(() => {
        this.showMessage2 = false;
      }, 3000);
    } catch (error) {
      console.error(error);
    }
},

async sendText() {
            const data = {
              number: localStorage.getItem('phone') || this.phoneNumber,
              message: 'Wow! You updated your account details, ' + this.name
            }
            axios.post('http://127.0.0.1:5000/send_sms', data)
              .then(response => console.log(response))
              .catch(error => console.log(error))
          },

sendFormsTogether(){
  this.sendText();
  this.updateUserProfile();
},


async updateUserProfile() {
    try {
      const response = await axios.post('http://localhost:5000/profile', {
        userID: localStorage.getItem('userID'),
        name: this.name,
        lastName: this.lastName,
        email: this.email,
        phoneNumber: this.phoneNumber,
        profileImage: this.profileImage
      });
      this.showConfirmationBox = false;
      this.showMessage = true;
      setTimeout(() => {
    window.location.reload();
  }, 1000);
      setTimeout(() => {
        this.showMessage = false;
      }, 3000);
    } catch (error) {
      console.error(error);
    }
  },
  reloadPage() {
    location.reload();
  }

    },
    computed: {
      isLoggedIn() {
        return this.$store.state.isLoggedIn;
      },
      username() {
        return this.$store.state.username;
      },
      enableTextNotifications() {
      return this.phoneNumber !== null;
      },
      enableEmailNotifications() {
        return this.email !== null;
      },
    },
    created() {
    this.getUserProfile(localStorage.getItem('userID'));
  }
  }
  </script>

  <style scoped>

.updatedMessage{
  position: relative;
  top: 18px;
}
.overlay {
  position: fixed;
  top: 0;
  width: 100%;
  height: 100%;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 3;
}
.confirmation-box {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.16);
  padding: 20px;
  z-index: 4;
}

.confirmation-message {
  text-align: center;
}

.confirmation-buttons {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.btn-confirm {
  background-color: #72b264;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  margin-right: 10px;
}

.btn-confirm:hover {
  background-color: #639458;
  color: white;
}

.btn-cancel {
  background-color: silver;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

.btn-cancel:hover {
  background-color: rgb(169, 169, 169);
  color: #fff;

}
.profile-picture-wrapper {
  position: relative;
}

.img-circle .change-profile-pic-overlay {
  display: none;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  color: white;
  background-color: rgba(0, 0, 0, 0.5);
  justify-content: center;
  align-items: center;
  font-size: 12px;
  border-radius: 100%;
  overflow: hidden;
  text-align: center;
}

.img-circle:hover .change-profile-pic-overlay {
  display: flex;
  cursor: pointer;
}
  
 .btn-custom{
  background-color: #72b264;
  color: white;
 }

 .btn-custom:hover{
  background-color: #6d9863;
  color: white;
 }



.nav-link {
  color: #474b4f;
}

.nav-link:hover {
  color: #000000;
}
  .nav-pills .nav-link.active, .nav-pills .show>.nav-link {
    background-color: #72b264;
    color: #fff;
}
.container{
  background-color: transparent;
  
}



.profile-tab-nav {
	min-width: 250px;
}

.tab-content {
  height: 400px; 
}

.form-group {
	margin-bottom: 1.5rem;
}

.nav-pills a.nav-link {
	padding: 15px 20px;
	border-bottom: 1px solid #ddd;
	border-radius: 0;
	color: #333;
}
.nav-pills a.nav-link i {
	width: 20px;
}

.img-circle {
  position: relative;
  display: inline-block;
  left: 60px;
}
.img-circle img {
	height: 80px;
	width: 80px;
	border-radius: 100%;
}
</style>