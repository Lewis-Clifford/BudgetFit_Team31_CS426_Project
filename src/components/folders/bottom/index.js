import React from 'react'
import { Wrapper, Email, Header, TheInput, UserInput, Inp, Btn} from './bottom'

const Bottom = () => {
  return (
    <Wrapper>
        <Email>
            <Header>
            Hello!
            </Header>
            <TheInput>
                <UserInput>
                    <Inp placeholder="Enter Email"/>
                    <Btn type="button">
                    Hi.
                    </Btn>
                </UserInput>
            </TheInput>
        </Email>
    </Wrapper>
  )
}

export default Bottom