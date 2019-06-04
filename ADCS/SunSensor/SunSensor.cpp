/**
 * @file   SunSensor.cpp
 * @version 1.0
 * @date 2019
 * @author Remy CHATEL
 * @copyright GNU Public License v3.0
 * @brief  Source code for the SunSensor Library
 * 
 * @details
 * # Description
 * This library provide an interface to read the analog output of
 * a set of three photodiodes that make a Sun sensor
 * 
 * @see SunSensor
 * 
 * # License
 * <b>(C) Copyright 2019 Remy CHATEL</b>
 * 
 * Licensed Under  GPL v3.0 License
 * http://www.gnu.org/licenses/gpl-3.0.html
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
 
#include "SunSensor.h"

SunSensor::SunSensor(){
    
}

SunSensor::SunSensor(AnalogIn* analogX, AnalogIn* analogY, AnalogIn* analogZ){
    faceX_ = analogX;
    faceY_ = analogY;
    faceZ_ = analogZ;
}

SunSensor::~SunSensor(void){
    
}

void SunSensor::getSunVector(float rsun[3]){
    rsun[0] = (*faceX_);
    rsun[1] = (*faceY_);
    rsun[2] = (*faceZ_);
}

float SunSensor::getXface(){
    return (*faceX_).read();
}

float SunSensor::getYface(){
    return (*faceY_).read();
}

float SunSensor::getZface(){
    return (*faceZ_).read();
}