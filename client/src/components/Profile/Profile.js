import React, { Component } from 'react';
import styled from 'styled-components';

const ProfileStyles = styled.div`
display: grid;
 grid-template-columns: 20% 80%;
 grid-template-rows: 1fr 1fr 1fr 1fr 1fr;
 justify-content: space-between;    

.one{
   display: grid;
   justify-content: center;
 .avatar{
       img{
               margin: 0 auto;
               height: 200px;
               width: 200px;
               margin-top: 20px;
               border-radius:50%;
       }
  }

}
`
const FlexContainer = styled.div`
       display: grid;
       grid-template-columns: 30% 20% 20% 30%;
       border: solid 5px;
       border-style: groove;
       height: 80px;
       width: 100%;
       padding: 10px;
       h5{
           font-weight: lighter;     
       }
       `
const FlexContainer2 = styled.div`
       display: grid;
       grid-template-columns: 30% 30% 30%;
       border: solid 3.5px;
       border-bottom: solid 7px;
       border-style: groove;
       border-bottom-style: groove;
       h5{
           font-weight: lighter;
       }
       span{
           color:green;
           font-weight: bold;
       }
       
       height: 200px;
       width: 100%;
       padding: 10px;
`
const ButtonStyles = styled.div`
button {
    background-color: #31A9E0;
    border: none;
    color: white;
    padding: 15px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 9px;
    font-weight: bold;   
    width: 100%;
    margin: 10px;
}
`
const Padding = styled.div`
margin-left: 10px;
`
const ROpadding = styled.div`
margin-top: 100px;
`
const ImageWrapper = styled.div`
display: grid;
justify-content: center;
img{
    border: solid 3px;
    border-radius:50%;
    height: 100px;
    width: 100px;
}
`
const ImageWrapper1 = styled.div`
display: grid;
justify-content: center;
img{
    padding:2px;
    margin-top: 50px;
    border: solid 3px;
    border-radius:50%;
    height: 100px;
    width: 100px;
}
`
class Profile extends Component {
    render() {
        return (
            <ProfileStyles>
                <div className="one">
                    <div className="avatar">
                        <img src="https://ga-core.s3.amazonaws.com/production/uploads/instructor/image/11753/thumb_12743681_10205360674872559_4950095949390533970_n.jpg" alt="Smiley face"></img>
                    </div>
                </div>
                <div className="two">
                    <div className='container'>
                        <ROpadding>
                            <h2>Recent Orders</h2>
                        </ROpadding>
                        <FlexContainer>
                            <div className="orderPlaced"><h5>Order Placed</h5></div>
                            <div className="total"><h5>Total</h5></div>
                            <div className="shipping"><h5>Shipping To</h5></div>
                            <div className="orderNumber"><h5>Order Number</h5></div>
                        </FlexContainer>
                    </div>
                </div>
                <div className="three">
                    <ImageWrapper1>
                        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQz4k7ySWXn8hTb7DmvwyvxetkqLN0yhEHiFBs23x4nEnDiY5I43Q" alt="My Orders"></img>
                      
                    </ImageWrapper1>
                </div>
                <div className="four">
                    <div className='container'>
                        <FlexContainer2>
                            <div className="Status"><h5>Status:<span>Shipped</span></h5></div>
                            <div className="Item"><h5>Item 1 of 2</h5></div>
                            <div className="Expected Delivery">
                                <Padding>
                                    <h5>Expected Delivery: Dec 19</h5>
                                </Padding>
                                <ButtonStyles>
                                    <button type="submit">Track Package</button>
                                </ButtonStyles>
                                <ButtonStyles>
                                    <button type="submit">Track Package</button>
                                </ButtonStyles>
                            </div>
                        </FlexContainer2>
                    </div>
                </div>
                <div className="five">
                    <ImageWrapper>
                         <img src="https://img.icons8.com/wired/2x/settings.png" alt="My Orders"></img>
                    </ImageWrapper>
                </div>
                <div className="six">
                    <div className='container'>
                        <div className="two">
                            <FlexContainer2>
                                <div className="Status"><h5>Status:<span>Shipped</span></h5></div>
                                <div className="Item"><h5>Item 2 of 2</h5></div>
                                <div className="Expected Delivery">
                                    <Padding>
                                        <h5>Expected Delivery: Dec 19</h5>
                                    </Padding>
                                    <ButtonStyles>
                                        <button type="submit">Track Package</button>
                                    </ButtonStyles>
                                    <ButtonStyles>
                                        <button type="submit">Track Package</button>
                                    </ButtonStyles>
                                </div>
                            </FlexContainer2>
                        </div>
                    </div>
                </div>
            </ProfileStyles>
        );
    }
}

export default Profile;